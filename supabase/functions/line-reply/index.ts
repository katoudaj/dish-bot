import { serve } from "https://deno.land/std/http/server.ts";

const GITHUB_TOKEN = Deno.env.get("GITHUB_TOKEN")!;
const REPO = "katoudaj/dish-bot";
const WORKFLOW_ID = "notify.yml"; // workflow ファイル名

serve(async (req) => {
  const body = await req.json();
  const event = body.events?.[0];

  if (!event || event.type !== "message") return new Response("ok");

  const userMessage = event.message.text;
  const userId = event.source.userId;

  console.log("LINEからの受信:", userMessage);
  console.log("送信者のuserId:", userId);

  // GitHub Actions workflow_dispatch を呼ぶ
  const response = await fetch(
    `https://api.github.com/repos/${REPO}/actions/workflows/${WORKFLOW_ID}/dispatches`,
    {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${GITHUB_TOKEN}`,
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        ref: "master",
        inputs: {
          message: userMessage,
          user_id: userId
        },
      }),
    }
  );

  // レスポンス確認用
  const text = await response.text();
  console.log("GitHub API response:", text);

  return new Response("ok");
});
