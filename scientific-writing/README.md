# Scientific Writing

A standalone skill for drafting and revising mathematical and scientific
papers. It focuses on the reader's problem, proof structure, precise claims,
and readable LaTeX. Contributed by Cunxin Huang, with proof guidelines from
Zaikun Zhang and source-based guidance from Knuth, Higham, and McEnerney.

## Review the skill

1. Start with [SKILL.md](SKILL.md), including the nine proof guidelines.
2. Inspect the [worked proof example](references/proofs-and-derivations.md).
3. Read the [extended style guide](references/style-guide.md) and
   [source notes](references/source-corpus.md) as needed.

The package contains the instructions, seven local reference files, agent
metadata, and two optional LaTeX log helpers. It needs no private documents,
account credentials, or connection to its contributor's machine. The full
books, manuscripts, private revision messages, and lecture captions are not
bundled.

## Try it with an agent

Copy this complete folder into the skill directory used by your agent, or
give the agent this request from the repository root:

```text
Read scientific-writing/SKILL.md and the relevant referenced files.
Revise the following passage for [audience], preserving its mathematical
claims and assumptions. Explain any consequential editorial choices.

[passage]
```

Hosts that discover `SKILL.md` can invoke it by the name `scientific-writing`.
The references are loaded as needed; they are not a mandatory reading list for
every edit. No helper needs to run for a prose-only revision.

For LaTeX log review, the optional scripts require Python 3.10+:

```bash
python3 scientific-writing/scripts/latex_overfull_report.py /path/to/build.log --min-pt 5
python3 scientific-writing/scripts/latex_vbox_report.py /path/to/build.log --min-badness 1000
```

Use the manuscript's existing build environment when compilation is needed.
Log reports guide inspection; the rendered pages still need review.

## Relation to TeX Polisher

The existing `tex_polisher/polisher.md` concentrates on grammar and Equipe Z
typesetting conventions. This skill addresses scientific exposition, argument
order, proofs, claim scope, and semantic preservation. They can be selected
together when both tasks are wanted; adding this skill does not change TeX
Polisher or silently apply its output format.

## Packaging and maintenance

The repository also provides `packages/scientific-writing.zip`, containing
a standalone copy of this folder. `MANIFEST.json` records the files and their SHA-256 hashes, excluding
the manifest itself. The ZIP contains no other skill.

This is a shared adaptation of the contributor's personal workflow. Personal
paths and revision history were replaced by portable instructions and public
source references. The nine proof guidelines are retained unchanged. Changes
to examples should preserve the mathematical content of the before/after
versions; see [maintaining.md](references/maintaining.md).
