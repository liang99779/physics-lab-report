# Report Standard

## Content fidelity

- Every experiment-specific claim must trace to the PPT, template, raw data, pre-lab report, or an explicit user statement.
- Never infer the specimen material, apparatus model, reference value, uncertainty, or environmental condition from a common version of the experiment.
- Distinguish measured values from calculated values and theoretical/reference values.
- Preserve raw-data order, decimal precision, sign, blank cells, and units.

## Formula rules

- All physical variables and mathematical symbols use native Word equation objects, including inline symbols and table entries.
- Subscripts and superscripts are structural equation elements, not manually lowered/raised text.
- Define symbols at first use when the source does not already make them obvious.
- Number only a newly introduced governing relation or a derived formula.
- Use one consecutive numbering sequence. Place the number at the right margin and keep the formula visually centered.
- Numerical substitution lines are unnumbered, even when several are displayed.

Example pattern:

1. Introduce and number the governing relation.
2. Derive and number a materially new relation.
3. Show each evaluation without a number, for example:

   `ΔL_1 = N_1 λ / 2 = 50 × 632.8 / 2 = 15820 nm`

The example illustrates structure only; use actual source values and units.

## Data-processing rules

- The processed table must correspond to both the original record and the PPT's required table topology.
- Every calculated number appearing in a table, graph, paragraph, conclusion, or check must have a visible formula substitution somewhere in the report.
- Do not use “同理可得” to hide repeated numerical work.
- Carry units through substitutions and state unit conversions.
- Apply one documented rounding/significant-digit convention consistently.
- Check arithmetic programmatically, but present it in readable mathematical form in the report.
- A graph uses processed values already shown in the report. Label both axes with quantity and unit, show useful point values where appropriate, and add a figure title/caption.

## Writing rules

### Report voice

- Use natural Chinese suitable for a student's submitted experiment report. State measurements, calculations, conclusions, and physical reasoning directly, without inventing observations or claiming procedures were performed when they were not recorded.
- Keep authoring commentary and source-selection explanations in working notes or the chat. Do not put phrases such as “课件中的直径示例不参与计算”, “采用课件给出的”, “预习题表明”, or “表格与代入行采用显示值” into the report body. For example, write “测得吊环内径、外径分别为……” or “取重力加速度为……”. This does not prohibit scientific citations when required.
- Report unresolved input conflicts to the user. Keep a brief scientific limitation in the report when it materially affects the result; do not hide uncertainty, missing measurements, or inconsistent data to make the wording sound more confident.

### Result statement

Keep 结果陈述 short. The default is one or two brief paragraphs of experimental conclusions, without an error-analysis paragraph. About 150–250 Chinese characters is a useful guide, not a hard limit; adapt to the experiment, template, and user's requested length.

The conclusion includes the relevant measurement range or condition, the main result with its unit, and a supported trend or consistency finding. Add a short scientific limitation only when needed to avoid overstating accuracy; this does not require a general error-analysis paragraph.

Do not repeat the derivation, every table value, apparatus dimensions already stated, or a catalogue of possible errors. Do not add an optional error-analysis heading when no analysis is warranted. If the template has a fixed error-analysis box, preserve its layout and leave its content empty unless the trigger below is met. Brevity here must not remove numerical substitutions from 数据处理.

### Error analysis

Omit error analysis by default. Add it only for an unusually large, evidence-supported discrepancy that materially undermines the experimental result, such as an order-of-magnitude disagreement with a reliable supplied reference, a physically impossible result, or a dominant abnormal measurement that changes the conclusion. First recheck transcription, units, and calculations. Judge severity against the actual experiment and any supplied precision or valid range; do not invent a universal percentage cutoff, reference value, or uncertainty.

Ordinary scatter, small deviations, generic possible error sources, or a single sign change in a weak signal do not by themselves meet this trigger. When it is not met, omit the analysis entirely: no added heading, generic paragraph, or filler such as “无明显误差”. Preserve the measurements and any brief limitation needed for an honest conclusion.

When the trigger is met, keep the analysis brief and connect the supported cause to its physical mechanism, its effect on the result, and the corresponding improvement. Distinguish a demonstrated cause from a possible one; do not guess the direction of an error or list unrelated causes.

This omission rule does not remove required numerical error or uncertainty calculations, or answers to explicit user requests and assigned thinking questions about errors. Complete those in their designated places without automatically adding a general error-analysis section.

### Thinking questions

Start with a direct answer, then organize the explanation so the reader can follow why it is true. Use a few grouped, numbered points when the question has parallel causes or factors; each point should be a connected causal explanation rather than a list of nouns.

- For an error-source question, group related causes by measurement stage or mechanism. In each point use cause → physical mechanism → effect on the measured quantity or calculated result → corresponding improvement. Explain how a reading becomes too large or too small where the direction is supported.
- For an influencing-factor question, name the factors first, then explain each as factor → change in the relevant physical property → consequence for the measured quantity. Add a control or comparison condition when it helps answer the question. Do not force an error remedy onto a purely theoretical question.
- For a conceptual or reasoning question, state the conclusion, explain the governing relation or mechanism, and finish with the relevant consequence or boundary condition.

Avoid disconnected fragments, repeated generic cautions, and vague statements such as “有误差” without an explanation. Keep each point focused and avoid repeating the entire result section.

## Layout rules

- Preserve the supplied template's page size, margins, border, cover, fonts, heading hierarchy, score blocks, signature areas, and required notes.
- Keep tables within margins; repeat header rows only when helpful and avoid splitting a logical row.
- Keep captions with their figures/tables and use the template's numbering style.
- Avoid large accidental blank areas, orphan headings, and unnecessary page breaks.
- In particular, sections 4 and 5 should flow continuously when space permits.
- Keep diagrams and raw-data photos legible without distortion.

## Final QA checklist

Before delivery, verify all of the following:

- [ ] Cover fields are correct and no placeholder text remains.
- [ ] Section order and labels follow the template.
- [ ] Every formula and physical symbol is a native equation object with correct indices.
- [ ] Formula numbers are consecutive and limited to introduced/derived formulas.
- [ ] Numerical substitution lines have no formula numbers.
- [ ] Every derived number is supported by an explicit substitution.
- [ ] The processing table matches the raw record and PPT cell by cell.
- [ ] Units, decimal places, and significant digits are consistent.
- [ ] No unsupported material or apparatus claim appears.
- [ ] 结果陈述 is concise and contains the principal conclusions; error analysis is absent unless a verified gross discrepancy meets the stated trigger, with no generic error-analysis filler.
- [ ] Thinking-question answers give a direct answer and a clear causal explanation, with logically grouped points when useful.
- [ ] No authoring notes or source-selection explanations remain in the report body; material scientific limitations are retained.
- [ ] No unwanted gap exists between sections 4 and 5.
- [ ] All DOCX pages have been rendered and visually inspected.
- [ ] The final PDF has no clipping, overlap, blank page, or broken equation.
- [ ] If supplied, the pre-lab report's first page is the unchanged final PDF page.

