# Operational guidance from the writing sources

Locators refer to the editions listed in `source-corpus.md`, not to a later
edition. These are paraphrases for practical use, not a substitute for
the books. The user's current instructions and explicit supervisor proof rules
govern this skill's choices when a source discusses alternatives.

## Knuth, Larrabee, and Roberts: Mathematical Writing

The 119-page course report reviewed for this skill is based on Stanford CS209 (1987).
Printed page 1 is PDF page 3. Apply §1 (printed pp. 1–6; PDF pp. 3–8):

- Join symbols and formulas with grammatical prose. Avoid a list of symbolic
  operations that leaves the reader to reconstruct the explanation.
- State a theorem with enough context and hypotheses to understand its claim;
  motivate the result rather than introducing it with an empty announcement.
- Define objects when introduced. A brief complementary description can make a
  definition understandable, but do not repeat the same information mechanically.
- Design each passage around what the reader already knows and expects next.
  Keep the prose's thread understandable on a first reading that skims formulas.
- Keep a single meaning for each symbol and consistent notation for an object.
  Minimize nested indices and avoid naming objects or elements unnecessarily.
- Display important formulas and identify targets/results that need later
  reference. Use words for prose-level logical links and punctuation for the
  mathematical sentence; do not insert a colon between a verb and its formula
  merely because the formula is displayed.
- Use parallel structures for parallel claims. Vary sentence rhythm without
  cycling through synonyms for a technical object. Avoid praise of one's own
  results and unexplained jargon.

The context of §31 (printed pp. 69–71; PDF pp. 71–73) emphasizes knowing what
to communicate and to whom, addressing the idea before surface wording, and
making proof structure explicit. The referenced §32/§33 handout pages in this
copy contain headings but no readable handout body on rendered inspection;
do not claim to have extracted rules from the missing handouts.

The source uses jokes, examples, and context-dependent opinions. Do not turn
every sentence into an absolute rule. In particular, vary sentence structure
while preserving technical terminology, and retain an explanation when the
reader needs it even if it repeats a formula in a complementary way.

## Higham: Handbook of Writing for the Mathematical Sciences

Use the **second edition (1998)** for these page locators. Verify formulas
against the printed page if text extraction or OCR is imperfect.

| Source locator | Operational rule |
|---|---|
| Ch. 1, printed pp. 2–3 | Write during the research process to expose missing reasoning; learn from criticism and carefully chosen examples of good writing. Keep language simple and direct. |
| §3.1, pp. 16–17 | Use theorem/lemma/corollary roles to expose logical importance and dependency; do not give every routine fact a formal title. |
| §3.2, pp. 17–18 | Give the proof's structure and key idea; keep the reader oriented about the target, useful reductions, and remaining work. |
| §§3.3–3.4, pp. 18–21 | Choose examples with a clear job. Define only useful concepts, near their first use, in a form that makes their meaning apparent. |
| §3.5, pp. 21–24 | Choose distinguishable, conventional, economical notation; use the representation that reveals structure. The FFT example on p. 23 illustrates how matrix factorization can expose a reduction. |
| §§3.6–3.7, pp. 24–28 | Use symbols for precision and structure, words for meaning and justification; display relations when they help the reader follow the argument, not simply because they are long. |
| §§3.8–3.9, pp. 28–33 | Make parallel results look parallel; punctuate mathematical expressions, avoid unused symbols, and give informative cross-references such as the name of a recurrence or bound. |
| §§6.1–6.2, pp. 78–80 | Identify the reader and rank the contributions. Organize for both the first reading and later reference. |
| §6.6, pp. 85–86 | Make the abstract self-contained, informative, and supported by the completed paper; state findings, rather than merely announcing that results are presented. |
| §6.8, pp. 87–89 | State the problem and what is achieved early. Trim generic openings; introduce definitions early only when they are needed to state the actual problem. |
| §§6.9–6.11, pp. 89–96 | State experiment purpose and reproducible conditions; report accuracy as well as cost where relevant. Guide the reader to the important features of a table and cite sources precisely. |
| §§6.12, 6.14, pp. 96–97 | A conclusion adds perspective, limitations, or a useful next question. An appendix holds needed detail that would interrupt the main argument. |
| §7.1 and Fig. 7.1, pp. 108–110 | Revise in several ways: argument order, prose flow, equation/text balance, consistency, support for claims, and references. |
| §7.5, pp. 120–122 | Remove redundant equations and an unnecessary contradiction setup; select the calculation needed for the target. The right amount of intermediate detail depends on the audience. |

## Context-dependent choices

- Higham offers phrases such as "easy" or "straightforward" to indicate an
  omission. In this workflow, give the concise reason or identity when a
  justification is needed; do not replace missing reasoning with such adjectives.
- Higham discusses both scalar and matrix/vector descriptions. The supervisor
  specifically prefers matrix/vector notation, with entrywise work only when
  necessary. Apply that preference while retaining essential coordinate arguments.
- The books' historical publication procedures, software versions, and journal
  policies are not current operating instructions. Check the actual project
  toolchain and venue requirements when those facts matter.
- Neither concision nor active voice overrides mathematical meaning or the
  reader's needs. Extra explanation is useful only when it explains purpose,
  interpretation, or justification.

## Applying the McEnerney course to scientific writing

The public automatic-caption transcript was reviewed; timestamps and limits
are in `source-corpus.md`. The key operational distinction is between writing
to discover an idea and arranging that idea for readers. Reorder exploratory
notes after the argument is understood. The reader should not have to follow
the author's false starts to find the result.

Make the paper answer a question that a particular reader community has reason
to care about. Identify what readers accept, what remains unresolved, and what
the actual result changes. Novelty alone does not supply that reason. A gap
can be a valid motivation when its consequences are made explicit; the course
does not justify banning all gap language or pretending that correct earlier
work is wrong.

A professional literature review relates sources to the problem and the
reader's likely doubts. It is not a record of the order in which the author
read them. Analyze successful examples in the target field for the work their
language performs. Do not mechanically insert "however", "anomaly", or
"important" to imply value that the evidence does not establish.

Explanation remains necessary in a proof. The course's contrast between
argument and explanation concerns audience and function; it is not a ban on
definitions, background, or mathematical explanation when needed. Use the
supervisor's nine rules to decide where that explanation belongs.
