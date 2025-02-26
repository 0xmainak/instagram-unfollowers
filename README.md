# Instagram Unfollowers Manager 🔍

An automated tool to identify and unfollow Instagram users who don't follow you back. Built with Python using the Instagrapi library.

## ✨ Features

- 🔍 Identifies users who don't follow you back
- 🤖 Automated unfollow process
- ⏱️ Smart delay between actions to avoid Instagram limits
- 🔐 Secure credential management using environment variables
- 📊 Real-time progress tracking

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/0xmainak/instagram-unfollowers.git
cd instagram-unfollowers
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:
```env
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```

## 🚀 Usage

Run the script:
```bash
python main.py
```

The script will:
1. Log in to your Instagram account
2. Fetch your followers and following lists
3. Identify users who don't follow you back
4. Begin unfollowing process with safe delays

## 📁 Project Structure

```
instagram-unfollowers/
├── src/
│   ├── functions/
│   │   ├── __init__.py
│   │   ├── instagram_client.py
│   │   └── unfollow_manager.py
├── .env
├── .gitignore
├── main.py
└── README.md
```

## ⚠️ Important Notes

- Use this tool responsibly
- Be aware of Instagram's rate limits
- Keep your credentials secure
- Don't share your `.env` file

## 🔒 Security

- Credentials are stored in `.env` file
- `.env` is included in `.gitignore`
- No hardcoded sensitive information

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚡ Quick Start

```python
from src.functions import InstagramClient, UnfollowManager

instagram = InstagramClient().login()
unfollow_manager = UnfollowManager(instagram)
unfollow_manager.unfollow_users()
```

## 🐛 Troubleshooting

- Check your Instagram credentials
- Ensure you have proper internet connection
- Verify Python dependencies are installed
- Make sure `.env` file is properly configured

