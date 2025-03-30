# 🤖 Daily ChatGPT Commit

This repository automates a **daily Git commit** that generates a commit message using **OpenAI's GPT model**. It runs every day at **9 AM UTC** via GitHub Actions and appends the AI-generated message to a `daily_log.txt` file.

---

## 📌 What It Does

- Uses a scheduled GitHub Action to run daily.
- Calls OpenAI's GPT-3.5 Turbo to generate a professional commit message.
- Logs the message in `daily_log.txt`.
- Commits and pushes the changes back to the `main` branch.

---

## 🧠 Powered by
- [GitHub Actions](https://github.com/features/actions)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- `gpt-3.5-turbo` for commit message generation.

---

## 🔧 Files Included

- **`.github/workflows/daily_commit.yml`**  
  Workflow file that schedules and runs the automation.

- **`scripts/daily_commit.py`**  
  Python script that interacts with the OpenAI API and appends the response to `daily_log.txt`.

- **`daily_log.txt`**  
  Log file storing all daily commit messages with UTC timestamps.

---

## 🔐 Secrets Required

Set the following repository secrets in GitHub:

| Secret Name         | Description                          |
|---------------------|--------------------------------------|
| `OPENAI_API_KEY`    | Your OpenAI API key                  |
| `GITHUB_TOKEN`      | Provided by GitHub by default        |

---

## 🚀 Setup Instructions

1. Clone or fork this repo.
2. Add your OpenAI API key to your repository secrets.
3. Customize the `prompt` in `daily_commit.py` if desired.
4. Enjoy automated, AI-generated daily commits!

---

## 🗓️ Schedule

The workflow is triggered:
- Automatically every day at **9:00 AM UTC**
- Manually via the GitHub **"Run workflow"** button

```yaml
cron: '0 9 * * *'  # Every day at 9 AM UTC
```

---

## 📄 Sample Log Output

```
2025-03-30 09:00:00 UTC: Refactored minor components for better clarity and performance.
`
```
### Deployment
Continuous automated commits trigger continuous deployment via GitHub Actions, enabling seamless updates.

## Contribution
Contributions to enhance predictive algorithms, optimize UI/UX, and improve automation scripts are welcome. Please follow standard GitHub contribution guidelines:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements
- [Flutter Documentation](https://flutter.dev/docs)
- [OpenAI Documentation](https://platform.openai.com/docs/api-reference)
- Community support and contributors.

