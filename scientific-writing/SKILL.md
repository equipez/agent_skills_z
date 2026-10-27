---
name: scientific-writing
description: Draft, revise, or audit mathematical and scientific papers, proofs, derivations, optimization manuscripts, and theses. Apply Zaikun Zhang's explicit proof rules, source-grounded Knuth and Higham guidance, reader-oriented argument design, and LaTeX layout review. Use for scientific writing polish, theorem-aware shortening, abstracts, introductions, literature reviews, and conclusions; pair with a project skill for its subject-specific definitions and evidence.
metadata:
  version: "2026-10-27"
---

# Scientific Writing

Help the reader understand the mathematical problem, the argument, and the exact
result. Preserve the author's mathematics and develop the author's judgment.
Use this skill for substantive scientific writing. Its style sources are
Zaikun Zhang's proof guidelines, Knuth--Larrabee--Roberts, Higham, the public
PDFO paper, and reader-oriented writing guidance associated with Larry McEnerney.

## Resolve the writing task

1. Read the requested passage, its surrounding argument, applicable project
   conventions, and the relevant source statement before rewriting. Identify
   the audience and the passage's job: motivation, definition, theorem, proof,
   experiment, limitation, or transition.
2. Identify the actual mathematical target and dependencies. Preserve
   assumptions, quantifiers, domains, events, modality, constants, strict versus
   non-strict inequalities, notation, citations, and logical direction. Treat
   uncertainty or a suspected mathematical error explicitly; do not polish it
   into an apparently established claim.
3. Fix argument order and missing explanations before polishing sentences.
   For proofs and derivations, apply **all nine rules below**. For positioning,
   first apply the reader-value pass. A short local edit does not require a
   whole-paper rewrite or a new experiment.
4. Revise with direct language and the least detail that makes the intended
   reasoning followable. Compare the revised passage against the original for
   mathematical equivalence and against the target for a complete argument.
5. For substantive LaTeX edits, compile when feasible, check references and the
   log, and inspect the affected PDF pages. Use
   [latex-layout-qa.md](references/latex-layout-qa.md) for the detailed checks.
   Use `latex-review-packet` when a rendered before/after comparison is useful
   and that companion skill is available.
6. Before handing a revision back for supervisor discussion, complete the final
   self-review below. Report the actual changes, validation, and unresolved
   mathematical questions. Explain consequential writing decisions briefly so
   the author can assess and learn from them.

## Style of proofs and mathematical derivations

These proof guidelines were provided by Zaikun Zhang. Apply them together
to proofs and mathematical explanations, including relevant explanations in
chat. Preserve their qualifications; they do not call for extra prose or full
expansion of routine algebra at every step.

1. Organize mathematical explanations around the reader's understanding. State the objective, explain any useful reduction, and give the main idea before presenting technical calculations. Explain how the assumptions support that idea when this helps orient the reader; defer technical details until they are needed.
2. Arrange the argument so that the purpose of each intermediate calculation is apparent when it appears. Let the order of the steps and the displayed mathematical relations reveal the logical progression. The reader should understand why a step is being taken before working through its details.
3. Introduce auxiliary notation when its purpose is apparent, and define it alongside the relation or construction it helps express.
4. Display the intermediate equations needed to follow the argument. Make the conditions justifying a transformation visible where they are used.
5. Match the detail to the audience. Explain transitions that would otherwise require the reader to reconstruct missing reasoning, and use concise identities for routine algebra.
6. Add prose when it clarifies purpose or justification. Avoid merely narrating operations that the displayed equations already make clear.
7. Calculate only what the argument needs.
8. Label important targets and intermediate results that will be referenced. Close the proof (or an intermediate stage of the proof) by explicitly connecting the established results to the target, without repeating reasoning already established.
9. Use matrix-vector notations whenever possible. Do not refer to entries of matrices or vectors unless truly necessary.

For application details and an original worked example, read
[proofs-and-derivations.md](references/proofs-and-derivations.md). In particular,
distinguish the **purpose** of a calculation from its **justification**. A valid
inequality can still be badly placed if the reader cannot see why it is needed.
Do not force a one-line identity into a multi-stage proof template.

## Reader-value pass

For an abstract, introduction, motivation, literature review, conclusion, or
proposal, establish the following before sentence-level polish:

- Who is the reader, and what mathematical or practical question matters to them?
- What is already established, and what precise limitation, boundary case,
  mismatch, or unresolved mechanism remains?
- What consequence does that limitation have for interpreting a theorem,
  implementing a method, or evaluating a result?
- What does this work establish, under what assumptions, and how does that
  change the reader's understanding?

Novelty, an unfilled gap, and the author's effort do not by themselves explain
value. Relate prior work to the question instead of listing papers. Keep the
motivation proportionate to the actual result. Do not manufacture a crisis,
invent a research gap, or force every paragraph into the same pattern.

The abstract should stand on its own and state actual findings with their
essential scope. The introduction should lead to the precise problem and the
main result, rather than postponing the answer for suspense. A conclusion
should give implications, limitations, or a useful next question instead of
repeating the abstract. See [book-guidance.md](references/book-guidance.md)
and [source-corpus.md](references/source-corpus.md) for source locators.

## Language, notation, and scientific scope

- Use plain, precise words and stable mathematical terms. Vary sentence
  structure when useful, without renaming the same object for stylistic variety.
- Make pronouns, demonstratives, and logical connectors refer to explicit
  objects or claims. Avoid noun piles and empty announcements of importance.
- Use a natural mixture of sentence lengths. Prefer one main logical job per
  sentence; mathematical scope takes priority over an arbitrary word limit.
  ASD-STE100 is a secondary structural aid, not a formal academic vocabulary or
  compliance requirement.
- Prefer direct verbs. Choose active or passive voice according to the
  mathematical subject and information flow; neither is universally required.
- Write prose around formulas as grammatical sentences. Punctuate displays
  accordingly. Use words for prose-level logical connections, rather than a
  string of implication symbols. Separate unrelated symbolic expressions with
  words. Avoid sentence openings that make a symbol ambiguous with a word.
- Define necessary objects close to use. Explain the meaning or consequence of
  an important formula when this adds understanding. Avoid unused symbols,
  gratuitous indices, and distinctions that are visually difficult to recognize.
- Make formal theorem statements understandable with their hypotheses and
  defined objects, using precise cross-references where needed. State sufficient
  hypotheses and boundary cases accurately. Do not promote
  "sufficient" to "necessary", a lower bound to an asymptotic equivalence, or
  positive probability to almost-sure behavior. Verify assumptions when applying
  an external theorem and cite its relevant location.
- Use "essential", "sharp", "optimal", and "equivalent" only with a clear
  supported scope. Avoid "obvious" and "easy" as substitutes for a needed
  reason. A concise identity can supply that reason without commentary.
- In numerical writing, state the experiment's question before the setup and
  result. Include conditions needed for interpretation and reproduction. Keep
  empirical support, proved statements, conjectures, and limitations distinct.
- Follow the manuscript's terminology and venue conventions. In optimization
  writing, prefer a precise method name to vague conceptual "black box" framing.

## Shortening without loss of reasoning

Delete empty metadiscourse, unsupported praise, duplicated roadmaps, repeated
contributions, and genuinely redundant background first. Use a precise
cross-reference where the local argument does not need a repeated statement.
Remove calculations whose results the proof never uses. Do not remove an
intermediate relation or explanation merely to reduce the word count when the
reader needs it to follow the argument.

Compare before and after: assumptions and quantifiers; claim strength; symbols,
indices, domains and event meanings; boundary cases; theorem and citation
references; proof dependencies; experiment conditions; and paragraph connections.
Reject unintended changes. For a broad shortening pass, read
[asd-ste-academic-adaptation.md](references/asd-ste-academic-adaptation.md).

## Learn from revisions

The author remains responsible for mathematical meaning and writing choices.
When the user supplies supervisor feedback, turn the reusable part into a
specific correction in this skill or its relevant reference, supported by the
original comment and a small before/after example when available. Keep a
paper-specific notation decision with that project; do not make it universal.
Resolve conflicts using the user's current directions and the actual context.

During a writing-skill update, check for duplicate or conflicting rules,
validate the edited skill, and report the change. Keep installation choices
within the requested scope. After one or two papers, review the accumulated
rules for stable principles and remove redundant advice; do not keep expanding
the checklist for every isolated wording change. Read
[maintaining.md](references/maintaining.md) for how to keep feedback
traceable and project-specific decisions scoped.

## Final self-review

- Can the intended reader identify the problem, target, main idea, and result?
- Does each nontrivial calculation have an apparent purpose and sufficient
  justification? Are needed intermediate equations and proof closure visible?
- Are auxiliary notation, labels, and matrix/vector expressions economical and
  clear? Is each component expansion necessary?
- Did the edit preserve all mathematical claims, assumptions, references, and
  evidence, including unresolved questions and limitations?
- Does the prose add purpose or justification instead of narrating visible
  algebra? Does the level of detail fit the reader?
- For LaTeX, were the actual affected pages inspected and build limitations
  reported? A clean source diff alone does not establish good layout.

For an abstract or introduction with suspected reader confusion, do a linear
cold read and record the unclear concepts, claims, or transitions. If an
independent cold-reader pass is requested or materially useful and delegation
is authorized, give a fresh reader only the passage and audience, without the
intended interpretation. State whether the check was independent.

## Further references

- [style-guide.md](references/style-guide.md): extended prose patterns,
  mathematical scoping, chapter transitions, and software prose.
- [book-guidance.md](references/book-guidance.md): operational Knuth and Higham
  guidance with verified section/page locators and context-dependent exceptions.
- [proofs-and-derivations.md](references/proofs-and-derivations.md): how to apply
  the nine proof rules without hiding reasoning or adding routine narration.
- [source-corpus.md](references/source-corpus.md): bibliographic sources and
  exemplar locators. The package works without private documents.
