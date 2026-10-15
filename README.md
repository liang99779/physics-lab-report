# Physics Lab Report

面向 Codex 的中文大学物理实验报告技能。根据实验课件、原始数据、Word 模板与可选的预习报告，指导代理完成可编辑的 DOCX 和经过页面检查的 PDF。

这是一个代理工作流技能，不是输入文件后独立生成报告的命令行程序。仓库提供技能说明和辅助结构检查脚本；完整制作过程由宿主代理及其文档工具执行。

## 核心规则

- 保留所提供模板的封面、栏目、页边距、边框与评分区。
- 逐格核对原始记录，不虚构测量值、仪器型号、材料或参考值。
- 物理符号与公式使用原生 Word 公式对象，计算显示实际数字代入、单位与结果。
- 结果陈述写清测量条件、主要结果和数据支持的趋势。
- 默认完全省略误差分析。只有核对后确认异常特别严重、足以影响主要结论时，才写简短且有依据的分析；普通波动、小偏差或单个弱信号变号不自动触发，也不补写“无明显误差”等占位文字。
- 对最终报告逐页渲染和检查；若提供预习报告，将其第一页原样附在最终 PDF 的末尾。

用户的明确要求优先于默认规则。课程明确要求的误差数值计算和误差类思考题仍须完成。

## 安装

下载本仓库，把仓库文件放入 Codex 的 `skills/physics-lab-report/` 目录，确保 `SKILL.md` 位于该目录根部。默认位置为 `~/.codex/skills/physics-lab-report/`；设置了 `CODEX_HOME` 时，使用该目录下的 `skills/physics-lab-report/`。已有同名技能时先保留原版本，再合并所需更新。

也可以在支持技能安装的 Codex 会话中提出：

```text
请安装 https://github.com/liang99779/physics-lab-report 中的技能，技能位于仓库根目录，安装名称为 physics-lab-report。
```

## 使用

向代理提供：

| 材料 | 用途 |
| --- | --- |
| 实验 PPT/PPTX | 实验目的、原理、仪器、步骤与思考题 |
| 原始数据或清晰照片 | 测量数值、符号、单位及实际实验条件 |
| Word 实验报告模板 | 页面设置、封面、章节与表格样式 |
| 预习报告 PDF，可选 | 补充背景及待附加的第一页 |

示例请求：

```text
使用 $physics-lab-report，根据我提供的课件、原始数据和 Word 模板完成实验报告。
请逐项展示计算代入过程，交付 Word 与 PDF；将预习报告第一页原样附在 PDF 最后。
```

## 所需能力

完整流程需要宿主具备演示文稿读取、Word/OOXML/OMML 编辑、PDF 处理以及文档渲染和视觉检查能力。技能说明引用 presentations、documents 和 PDF 工作流；这些外部技能、Microsoft Office、LibreOffice、Poppler 等工具不随本仓库分发，应由使用环境提供适用的工具。

只有运行辅助检查脚本时才需要本仓库的 Python 依赖：

```bash
python -m pip install -r requirements.txt
```

检查脚本使用 Python 3.10 或以上版本。仅检查 DOCX 时使用 Python 标准库；检查 PDF 时需要 `pypdf`。

```bash
python scripts/inspect_report.py --docx report.docx --pdf report.pdf
python scripts/inspect_report.py --docx report.docx --pdf report.pdf --prep-pdf prelab.pdf
```

脚本输出 JSON，并在检测到结构问题时返回非零退出状态。检查项包括指定章节是否存在、Word 公式对象数量、占位文本及 PDF 页数。

**结构检查不能证明报告正确。** 脚本不会验证计算算术、测量数据一致性、公式物理意义、实验身份或页面排版。预习页检查仅比较页面尺寸和提取文本，不能证明扫描图片或页面视觉内容完全相同；仍须逐页渲染检查，必要时做像素比较。

## 文件结构

```text
SKILL.md                       技能入口
agents/openai.yaml             Codex 显示信息与调用设置
references/workflow.md         制作流程
references/report-standard.md  内容、公式、结果陈述与排版规则
scripts/inspect_report.py      辅助结构检查
requirements.txt               PDF 检查所需依赖
LICENSE                        MIT 许可证
```

## 发布范围

仓库仅包含通用技能说明和辅助代码，不包含实际学生报告、身份信息、原始记录照片、课程课件、学校模板或第三方工具。使用者应自行提供有权使用的材料。

## 许可证

本仓库内容采用 [MIT License](LICENSE)。使用者另行提供的课程资料、模板、实验记录及外部依赖不属于该许可证的授权范围。
