# vibecoding-baton

会话一长，token 在烧，回复在变钝。`/clear` 能把锐度找回来，也会把刚谈妥的下一步清掉。

**vibecoding-baton** 在会话过长、当前工作告一段落时，由 agent 生成下一会话的续作指令，并提示执行 `/clear`。无需手写交接，也无需粘贴 prompt。清空后，新会话直接续上。

Claude Code · Codex · [MIT](LICENSE) · 中文 · [English](README.en.md)

## 例子

给一个已上线的 SaaS 加团队账单：改 schema、写结算 API、接 Stripe webhook、再改管理后台。一天干不完。

**会话 1。** schema 和结算 API 已经落地，测试也过了。上下文很长，补 webhook 时开始漏边界条件。阶段收住了，agent 写好续作指令，提示你可以 `/clear`。

你输入：

```text
/clear
```

**会话 2。** 新会话直接带着这些约束开工：先读 `prisma/schema.prisma` 和 `apps/api/src/billing.ts`；只用 Stripe test mode；下一步是 webhook 幂等，不要重开 schema。它接着写 webhook，不再问「我们做到哪了」。

看到 `vibecoding-baton: baton passed`，就是交到了。没看到的话，剪贴板里有同一份指令。同一项功能可以这样接力多次。

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
