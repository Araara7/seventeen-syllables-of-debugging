# Seventeen Syllables of Debugging

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Araara7/seventeen-syllables-of-debugging/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Araara7/seventeen-syllables-of-debugging/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

Entry for the [Seventeen Syllables of Debugging](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605) bounty on make.fun.

## The haiku

> breakpoint never hits
> the stack trace points to nowhere
> it was my typo

Three lines, 5-7-5 syllables, 70 characters. A breakpoint that never fires, a stack trace pointing at nothing — and the last line turns it: the bug was a typo all along.

## How it works

`main.py` writes the haiku to `/output/entry.txt` and verifies the bytes on disk match exactly. It asserts the entry is three lines and 1–200 characters.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
