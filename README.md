# vibecoding-baton

会话一长，token 在烧，回复在变钝。`/clear` 能把锐度找回来，也会把刚谈妥的下一步清掉。

**vibecoding-baton** 让你清上下文，不清进度。`/baton` 写好下一棒，同一窗口 `/clear`，新会话已经拿着棒，接着干。

Claude Code · Codex · [MIT](LICENSE) · 中文 · [English](README.en.md)

## 用法

```text
/baton
/clear
```

看到 `vibecoding-baton: baton passed`，就是交到了。

没看到也没关系，剪贴板里有一份同样的提示。

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

`/baton` 把下一会话该读的文件、已做的决定、还不能丢的约束、下一步动作写成一段短提示，停在本机。

`/clear` 时注入一次，然后删掉。换项目不会串；重启、resume 也不会把棒提前吃掉。

数据只在你这台机器上，默认目录是 `~/.vibecoding-baton/handoffs/`。

## License

[MIT](LICENSE)
