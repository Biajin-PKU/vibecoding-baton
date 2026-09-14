# vibecoding-baton

<p align="center">
  <img src="assets/logo.png" width="280" alt="vibecoding-baton">
</p>

在 vibe-coding 会话之间传接力棒。

同时支持 **Claude Code** 和 **Codex**。skill 负责写下一会话的 prompt；hook 在 `/clear` 后注入一次。

中文 | [English](README.en.md)

## 为什么是 plugin

skill 只能把 prompt 写出来。`/clear` 之后自动注入，必须靠 SessionStart hook。两样一起发。

## 用法

1. 一个阶段做完，跑 **`/baton`**。
2. 在**当前窗口**输入 **`/clear`**。
3. 看到 `vibecoding-baton: baton passed` 就成功了。停放的 prompt 注入一次后删除。

没看到这条提示，用剪贴板里的备份。

## 安装

需要 Python 3。

### Claude Code

```text
/plugin marketplace add Biajin-PKU/vibecoding-baton
/plugin install vibecoding-baton@vibecoding-baton
```

本地目录：

```text
claude plugin install /path/to/vibecoding-baton
```

### Codex

把本目录当作 plugin 接入（skills + hooks）。hook 文件是 `hooks/hooks.json`。

## 槽位怎么算

停放和注入都用 `$CLAUDE_PROJECT_DIR`（没有再用 cwd）做哈希。末尾斜杠会去掉，`/proj` 和 `/proj/` 是同一个槽。

文件在 `~/.vibecoding-baton/handoffs/`。可用 `VIBECODING_BATON_DIR` 改路径。

hook 的 matcher **只匹配 `clear`**。后面的 `startup` / `resume` 不会把文件提前吃掉。

## 目录

```text
.claude-plugin/plugin.json
.codex-plugin/plugin.json
hooks/baton.py
hooks/hooks.json
skills/baton/SKILL.md
```

## 许可

MIT
