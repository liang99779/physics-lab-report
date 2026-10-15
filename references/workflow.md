# Workflow

## 1. Classify the sources

Assign each supplied file one role before extracting content:

| Source | Authority |
|---|---|
| User request and corrections | Highest authority for the requested outcome and personal conventions |
| Report template | Layout, section order, page setup, cover fields, tables, scoring blocks, and visual style |
| Experiment PPT | Experiment-specific purpose, principle, apparatus, formulas, procedure, expected data organization, and thinking questions |
| Raw record/photo/spreadsheet | Measured values, sequence, units, sample labels, and observations |
| Pre-lab report | Supporting experiment context and the page to append; it does not override newer measured data |
| Past completed reports | Style and workflow examples only; never copy experiment-specific facts blindly |

When sources conflict, preserve the conflict in working notes, follow the highest applicable authority, and disclose any unresolved ambiguity that affects the result.

## 2. Inspect before editing

Read the full PPT, the full template topology, every raw-data cell, and the relevant pre-lab pages. Render source pages or slides when layout, equations, diagrams, or handwriting matter. Build a compact fact sheet containing:

- identity fields required by the cover;
- experiment title and section headings;
- known constants with units and precision;
- measured data exactly as recorded;
- formulas and symbol definitions;
- required tables, charts, images, and questions;
- facts that are explicitly not supplied.

Do not begin calculations until the transcribed measurements have been checked against the source image or table.

## 3. Plan the calculations

Create a dependency list from measured values to each derived value. For every output quantity, record:

- source measurements;
- governing formula;
- unit conversion;
- substitution line;
- rounding/significant-digit rule;
- destination table cell or chart point.

Calculate independently from the PPT's illustrative numbers unless the PPT explicitly states that they are the user's data. Cross-check repeated calculations with a second method when practical, such as comparing interval averages with a cumulative calculation.

## 4. Author in the supplied template

Make a working copy of the template rather than rebuilding it. Fill the cover and sections without changing protected layout elements. Adapt content density to the existing page design.

Recommended report order when the template permits it:

1. 实验目的
2. 实验原理
3. 实验仪器
4. 实验内容与步骤
5. 数据处理
6. 结果陈述
7. 思考题
8. 原始数据记录页（若模板要求）

The template remains authoritative if its labels or order differ.

## 5. Build native equations

Create Word OMML equation objects for inline physical symbols and displayed mathematics. Keep equation numbers right-aligned in the template's style. Introduced or derived equations use consecutive numbers such as `(1)`, `(2)`, `(3)`. Numerical substitutions beneath them have no number.

Tables containing variables such as `T_i`, `N_i`, `ΔL_i`, `α_i`, `λ`, or scientific-notation powers must also use equation objects in the relevant cells. Use ordinary text for prose and conventional unit labels when no mathematical typesetting is needed.

## 6. Populate data treatment

First reproduce the raw/processed table required by the PPT and original record. Preserve column order and leave genuinely unmeasured cells blank. Then show each calculation beneath or beside the table in a readable sequence.

For repeated intervals, write every substitution explicitly. Do not collapse five results into “同理可得”. Include averages, cumulative checks, coordinates used for plots, slopes/intercepts when used, uncertainty or relative error when the source provides a reference value, and any other number that appears in the conclusion.

## 7. Write conclusions and thinking answers

Apply the compact result statement and causal thinking-answer patterns in [report-standard.md](report-standard.md#writing-rules). Keep 结果陈述 focused on the principal result, measurement conditions, and supported trends. Omit error analysis unless the gross-error trigger in that reference is met; leave detailed calculations in 数据处理 and required conceptual explanations in 思考题.

Before rendering, remove prose about how the report was written, which example values were excluded, or how source files were selected. Report unresolved source conflicts to the user, while retaining any scientific limitation that materially affects interpretation of the result.

## 8. Render, repair, and export

Render the DOCX to page images and inspect every page at readable resolution. Repair spacing, clipping, equation alignment, table overflow, split rows, blank pages, and excessive gaps. Pay special attention to the boundary between sections 4 and 5; do not insert a page break unless the template requires one.

Export the verified report to PDF. If the raw record must be attached, include it in the report or as its designated attachment page. If a pre-lab report is supplied, append only its first page, unchanged, after all report pages.

## 9. Final verification

Perform all checks in [report-standard.md](report-standard.md). Render the combined PDF and inspect every page again. Compare the appended final page with the pre-lab source page at the same resolution; they should be visually identical.

