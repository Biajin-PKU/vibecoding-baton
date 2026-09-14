# vibecoding-baton

会话一长，token 在烧，回复在变钝。`/clear` 能把锐度找回来，也会把刚谈妥的下一步清掉。

**vibecoding-baton** 让 agent 自己盯着这件事。上下文够沉、一个阶段也收住了，它会把下一棒停好，然后告诉你：可以 `/clear` 了。你不用写交接，也不用再贴一段 prompt。清完，新会话已经拿着棒。

Claude Code · Codex · [MIT](LICENSE) · 中文 · [English](README.en.md)

## 你要做的

装上。继续干活。

到点了，agent 会说可以清。你输入：

```text
/clear
```

看到 `vibecoding-baton: baton passed`，就是交到了。没看到的话，剪贴板里有同一份提示。

## 安装

需要 Python 3。

**Claude Code** — 分两条发送：

```text
/plugin marketplace add Biajin-PKU/vibecoding-baton
/plugin install vibecoding-baton@vibecoding-baton
```

**Codex**

```bash
codex plugin marketplace add Biajin-PKU/vibecoding-baton
codex plugin add vibecoding-baton@vibecoding-baton
```

新开一个会话。若提示启用 hook，选接受。

## 它做什么

会话变长时，hook 会提醒 agent：别打断手头的活；下一个阶段边界，把下一棒写好。

下一棒是一段短提示：该读的文件、已做的决定、还不能丢的约束、下一步动作。停在你这台机器上。

你 `/clear` 时注入一次，然后删掉。换项目不会串；重启、resume 也不会把棒提前吃掉。

默认目录：`~/.vibecoding-baton/handoffs/`。

## License

[MIT](LICENSE)
