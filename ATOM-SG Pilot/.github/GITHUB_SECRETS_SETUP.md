# GitHub Secrets Setup for Telegram Notifications

## Required Secrets

Add these secrets to your GitHub repository:

### 1. TELEGRAM_BOT_TOKEN
**How to get:**
1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot` command
3. Follow prompts to create a bot
4. Copy the HTTP API token (looks like: `123456789:ABCdefGHIjklMNOpqrSTUvwxyz`)

**Set in GitHub:**
- Go to: Repository Settings → Secrets and variables → Actions
- Click: New repository secret
- Name: `TELEGRAM_BOT_TOKEN`
- Value: Your bot token

### 2. TELEGRAM_CHAT_ID
**How to get:**

**Option A - Using the bot:**
1. Add your bot to this group chat (Zcaeth OpenClaw)
2. Send a message in the group
3. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
4. Look for `"chat":{"id":-1003889017461,...` (this is your chat ID)

**Option B - Using @userinfobot:**
1. Message [@userinfobot](https://t.me/userinfobot)
2. Forward a message from this group
3. It will show the chat ID

**Set in GitHub:**
- Name: `TELEGRAM_CHAT_ID`
- Value: `-1003889017461` (this group's ID)

## Verification

Test the setup by pushing a commit to any branch. You should receive a Telegram message.

## Troubleshooting

**No notifications received:**
1. Check GitHub Actions logs for errors
2. Verify bot is added to the group
3. Verify bot has permission to send messages
4. Check that secrets are spelled exactly as shown

**Wrong chat ID:**
- Group chats always start with `-100`
- Personal chats are just numbers (no `-100`)

## Security Note

Never commit these values to the repository. Always use GitHub Secrets.
