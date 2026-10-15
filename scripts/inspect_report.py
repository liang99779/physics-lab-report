#!/usr/bin/env python3
"""Run lightweight structural checks on a generated physics lab report."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
DEFAULT_SECTIONS = (
    "实验目的",
    "实验原理",
    "实验仪器",
    "实验内容与步骤",
    "数据处理",
    "结果陈述",
    "思考题",
)


def inspect_docx(path: Path, sections: tuple[str, ...]) -> dict:
    with zipfile.ZipFile(path) as archive:
        document_xml = archive.read("word/document.xml")
    root = ET.fromstring(document_xml)
    visible_text = "".join(node.text or "" for node in root.iter(f"{{{W_NS}}}t"))
    normalized = re.sub(r"\s+", "", visible_text)
    missing_sections = [section for section in sections if section not in normalized]
    equations = sum(1 for _ in root.iter(f"{{{M_NS}}}oMath"))
    equation_paragraphs = sum(1 for _ in root.iter(f"{{{M_NS}}}oMathPara"))
    tables = sum(1 for _ in root.iter(f"{{{W_NS}}}tbl"))
    drawings = sum(1 for _ in root.iter(f"{{{W_NS}}}drawing"))
    placeholders = sorted(set(re.findall(r"\[(?:TODO|待填|待补)[^\]]*\]", visible_text, flags=re.I)))
    return {
        "missing_sections": missing_sections,
        "equation_objects": equations,
        "display_equation_objects": equation_paragraphs,
        "tables": tables,
        "drawings": drawings,
        "placeholders": placeholders,
    }


def inspect_pdf(path: Path, prep_path: Path | None) -> dict:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError("pypdf is required for PDF inspection") from exc

    report = PdfReader(path)
    result = {"pages": len(report.pages)}
    if prep_path is not None:
        prep = PdfReader(prep_path)
        if not prep.pages:
            result["prep_first_page_matches_final"] = False
            result["prep_check_reason"] = "pre-lab PDF has no pages"
        elif not report.pages:
            result["prep_first_page_matches_final"] = False
            result["prep_check_reason"] = "report PDF has no pages"
        else:
            source = prep.pages[0]
            final = report.pages[-1]
            source_box = tuple(float(v) for v in source.mediabox)
            final_box = tuple(float(v) for v in final.mediabox)
            source_text = re.sub(r"\s+", "", source.extract_text() or "")
            final_text = re.sub(r"\s+", "", final.extract_text() or "")
            result["prep_first_page_matches_final"] = (
                source_box == final_box and source_text == final_text
            )
            result["prep_check_note"] = (
                "Structural/text comparison only; also render both pages and compare visually."
            )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docx", type=Path)
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--prep-pdf", type=Path)
    parser.add_argument("--sections", nargs="*", default=list(DEFAULT_SECTIONS))
    args = parser.parse_args()

    if not args.docx and not args.pdf:
        parser.error("provide --docx and/or --pdf")
    if args.prep_pdf and not args.pdf:
        parser.error("--prep-pdf requires --pdf")

    findings: dict[str, object] = {}
    errors: list[str] = []

    if args.docx:
        findings["docx"] = inspect_docx(args.docx, tuple(args.sections))
        docx_result = findings["docx"]
        assert isinstance(docx_result, dict)
        if docx_result["missing_sections"]:
            errors.append("required section headings are missing")
        if docx_result["equation_objects"] == 0:
            errors.append("no native Word equation objects were detected")
        if docx_result["placeholders"]:
            errors.append("placeholder text remains")

    if args.pdf:
        findings["pdf"] = inspect_pdf(args.pdf, args.prep_pdf)
        pdf_result = findings["pdf"]
        assert isinstance(pdf_result, dict)
        if pdf_result["pages"] == 0:
            errors.append("PDF has no pages")
        if args.prep_pdf and not pdf_result.get("prep_first_page_matches_final"):
            errors.append("final PDF page does not structurally match pre-lab page 1")

    findings["errors"] = errors
    print(json.dumps(findings, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

