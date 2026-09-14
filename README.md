# vibecoding-baton

会话一长，token 在烧，回复在变钝。`/clear` 能把锐度找回来，也会把刚谈妥的下一步清掉。

**vibecoding-baton** 在会话过长、当前工作告一段落时，由 agent 生成下一会话的续作指令，并提示执行 `/clear`。无需手写交接，也无需粘贴 prompt。清空后，新会话直接续上。

Claude Code · Codex · [MIT](LICENSE) · 中文 · [English](README.en.md)

## 流程

场景：给已上线的 SaaS 加团队账单。schema 和结算 API 已经落地，测试通过。会话很长，接着写 Stripe webhook 时开始漏边界条件。

**1. 终端里弹出什么**

当前会话还在这个窗口。agent 先把续作指令写好，然后告诉你：

```text
结算 API 已落地，测试通过。下一会话从 Stripe webhook 幂等接着做。
现在可以 /clear。
```

**2. 人做什么**

不要新开终端，不要复制，不要粘贴。在**同一个窗口**输入：

```text
/clear
```

**3. 中间发生了什么**

`/clear` 清空当前上下文。hook 把刚才停好的续作指令注入新会话，注入一次后删除。终端出现：

```text
vibecoding-baton: baton passed
```

没看到这行时，同一份指令已在剪贴板。

**4. 新会话里人做什么**

还是这个窗口，已经是新会话。人不用再交代进度。直接继续说需求即可，例如「接着做」。agent 已经带着约束开工：先读 `prisma/schema.prisma` 和 `apps/api/src/billing.ts`，只用 Stripe test mode，下一步是 webhook 幂等，不要重开 schema。它不会问「我们做到哪了」。

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
