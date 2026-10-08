A text section: a numbered monospace label in a left rail, with paragraphs beside it.

- Provide a two-digit number, a short label and one or more paragraphs. Type the label in sentence case; CSS capitalises it.
- Number sections in page order, starting from 01. The number is `ink` and the rest of the label is `ink-muted`.
- The label is the section's `h2`, so the heading outline stays correct.
- Paragraphs stay within `measure`. Do not let text run the full column width.
- On a narrow screen the label stacks above the body. This comes from flex wrapping, so it needs no media query.
- A section holding work cards is different: put the label on its own line above, and let the cards span the full column.
