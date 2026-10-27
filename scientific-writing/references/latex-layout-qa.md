# LaTeX Layout QA

For substantive LaTeX edits, check the rendered PDF as well as the source. Apply the full-document pass when the user requests a final manuscript or thesis audit. Use the LaTeX log and visual PDF inspection as evidence, not only source review.

1. Compile the manuscript after substantive edits whenever feasible.
2. Parse the log for `Overfull \hbox` and inspect every warning in the edited files. Use `scripts/latex_overfull_report.py` when a project log is available.
3. Treat any `Overfull \hbox > 5pt` as requiring human inspection. Treat any `> 20pt` as blocking unless the rendered PDF proves it is harmless.
4. Displayed formulas must not overflow the text block or break accidentally. If a formula is too wide, rewrite it with `aligned`, `split`, `multline`, `alignedat`, a named intermediate quantity, or shorter prose around it.
5. Long inline formulas should usually become displayed formulas or named quantities. High-risk patterns include `\sum`, `\prod`, `\PP(...)`, `\EE(...)`, `\min\{...\}`, `\limsup`, and long logarithmic expressions.
6. Captions must be allowed to wrap. Do not wrap full caption sentences in `\mbox`, `\makebox`, or `\hbox`.
7. Theorem, lemma, proposition, and remark boxes need separate inspection because the effective text width can be smaller than the normal text block.
8. `\texttt{...}`, file names, option names, solver names, and long code identifiers must be made breakable or moved out of long prose sentences.
9. Item labels followed by long formulas are risky. Put the label on a short sentence, then display the formula if needed.
10. Treat `\paragraph{...}` followed by inline math as a high-risk reduced-width context; inspect these lines in the PDF.
11. Avoid `\mbox`, `\makebox`, and `\hbox` in prose, proof text, captions, item labels, and cross-reference ranges. Keep them only in deliberate macro definitions or administrative layout code, and inspect the rendered output.
12. Long cross-reference ranges are high risk. Do not hide them in boxes; split them into sentences or name the proof ingredients.
13. Keywords blocks, abstracts, theorem boxes, captions, and itemized lists are reduced-width contexts. Use `\raggedright`, shorter labels, or separate sentences when they contain long terms.
14. Hyphenated technical compounds are line-break risks, especially in lists and narrow environments: `non-convergence`, `random-series`, `multi-objective`, `p-probabilistic`, `sphere-polling`, and similar phrases. Rewrite them or shorten the sentence when they trigger overfull boxes.
15. Capture build stdout/stderr, not only `thesis.log`, and inspect driver warnings such as `xdvipdfmx:warning`, duplicate PDF anchors, undefined references, multiply-defined labels, and citation warnings.
16. Do not use `\nonumber` or `\notag` inside a single `equation` environment. Use `equation*`, `\[...\]`, or an `align`/`aligned` structure instead; otherwise hyperref can create duplicate equation anchors.
17. Check punctuation around displayed formulas. A displayed equation that ends a sentence should end with a period; do not leave a comma before a new sentence.
18. Do not ignore `Underfull \vbox` warnings in a final thesis pass. They often indicate bad page breaks, large vertical holes, isolated headings, orphaned display equations, or floats forcing awkward whitespace. Inspect the worst pages visually. Badness alone is not blocking; table-of-contents pages, lists, chapter-opening pages, and intentional blank pages may be harmless.
19. Float, table, figure, and front-matter QA are part of thesis polish. Inspect subcaption collisions, table width, figure placement, list of figures/tables, acronym/nomenclature pages, bookmarks, page numbering, and unintended blank pages.
20. For repository-level thesis passes, scan dormant source files in `content/` too, not only files included by `thesis.tex`. Unused chapters can reintroduce stale wording when they are included later.
21. Before declaring a thesis pass complete, report all `>20pt` overfull warnings, all `>5pt` warnings in edited files, and any visually bad underfull-vbox pages.
22. Render and inspect the PDF pages corresponding to the largest overfull warnings and worst page-break warnings, especially the top ten warnings after a full-thesis edit.

Risk scans:

```bash
rg -n -F '\mbox' /path/to/project/content /path/to/project/utils
rg -n -F '\makebox' /path/to/project/content /path/to/project/utils
rg -n -F '\hbox' /path/to/project/content /path/to/project/utils
rg -n '\\texttt\{[^}]{18,}\}|\\paragraph\{[^}]+\}.*\$|\\item .*\\textbf\{[^}]{24,}\}' /path/to/project/content
rg -n 'non-convergence|random-series|multi-objective|p-probabilistic|sphere-polling' /path/to/project/content
rg -n 'black-box|black box|fundamental|essential|sharp|novel|significant|dramatically|remarkably' /path/to/project/content
rg -n -U '\\begin\{equation\}[^\\]*(\\nonumber|\\notag)' /path/to/project/content
rg -n 'undefined|multiply defined|already defined|xdvipdfmx:warning|Citation|Reference' /path/to/build-output.log /path/to/project/thesis.log
rg -n '\\end\{equation\}|\\end\{align|\\end\{gather|\\end\{multline' /path/to/project/content
rg -n 'Underfull \\\\vbox|Overfull \\\\vbox' /path/to/build-output.log /path/to/project/thesis.log
```

Example:

```bash
python3 <skill-dir>/scripts/latex_overfull_report.py \
  /path/to/thesis.log --root /path/to/project --min-pt 5 --limit 20
python3 <skill-dir>/scripts/latex_vbox_report.py \
  /path/to/thesis.log --min-badness 1000 --limit 20
```
