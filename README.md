# 🔮 AWS Certified Cloud Practitioner CLF-C02 2025: AI-Powered Study Companion

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.49.0-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎯 Overview

Meet **Dr. CloudWise** - your dedicated AI mentor for AWS Certified Cloud Practitioner (CLF-C02) exam preparation! This intelligent Streamlit chatbot is specifically designed to help you master the foundational concepts of AWS Cloud Computing and ace your certification exam.

Unlike generic AI assistants, Dr. CloudWise is laser-focused on CLF-C02 exam content and will politely redirect you back to Cloud Practitioner fundamentals if you venture into advanced topics or other certifications.

### ✨ Key Features

- 🎓 **Exam-Focused Learning**: Aligned with all four CLF-C02 exam domains
- 🤖 **AI-Powered Mentoring**: Powered by OpenAI's GPT-4o-mini for intelligent responses
- 📚 **Structured Learning Path**: Progressive explanations from basic to intermediate concepts
- ❓ **Practice Questions**: CLF-C02-style questions to test your knowledge
- 🎯 **Scope Protection**: Automatically redirects off-topic questions back to exam content
- 💬 **Interactive Chat**: Real-time conversation with streaming responses
- 🔄 **Session Memory**: Maintains context throughout your study session

## 📋 CLF-C02 Exam Domains Covered

| Domain                    | Weight | Topics Covered                                                       |
| ------------------------- | ------ | -------------------------------------------------------------------- |
| **Cloud Concepts**        | 24%    | Benefits of AWS Cloud, Well-Architected Framework, Deployment models |
| **Security & Compliance** | 30%    | Shared Responsibility Model, IAM basics, Security best practices     |
| **Cloud Technology**      | 34%    | Core AWS services, Global infrastructure, Support plans              |
| **Billing & Pricing**     | 12%    | Pricing models, Cost optimization, Billing tools                     |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Basic understanding of command line

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/aws-cloud-practitioner-chatbot.git
   cd aws-cloud-practitioner-chatbot
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv env

   # On Windows
   env\Scripts\activate

   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure OpenAI API Key**

   Create a `.streamlit/secrets.toml` file in your project root:

   ```toml
   OPENAI_API_KEY = "your-openai-api-key-here"
   ```

   > 🔑 **Get your API key**: Visit [OpenAI API Keys](https://platform.openai.com/api-keys)

5. **Validate your setup** (Optional)
   ```bash
   streamlit run src/validate_credentials.py
   ```

## 🎮 Run the Application

Launch your AI study companion:

```bash
streamlit run src/awscloud.py
```

The app will open in your default browser at `http://localhost:8501`

## 💡 How to Use

1. **Start a conversation**: Type your AWS Cloud Practitioner question in the chat input
2. **Ask about exam topics**: Focus on CLF-C02 domains like:

   - "What is the AWS Shared Responsibility Model?"
   - "Explain the different EC2 instance types for the exam"
   - "What are the AWS Well-Architected Framework pillars?"
   - "How does AWS pricing work for beginners?"

3. **Get redirected if off-topic**: Dr. CloudWise will politely guide you back to exam-relevant content
4. **Practice with questions**: Ask for practice questions to test your knowledge
5. **Build on previous questions**: The chat maintains context throughout your session

### 📝 Example Interactions

```
👤 User: What is Amazon S3?

🤖 Dr. CloudWise:
**SERVICE**: Amazon S3 (Simple Storage Service)
**EXAM RELEVANCE**: Domain 3 - Core AWS service, heavily tested
**SIMPLE DEFINITION**: Secure, durable cloud storage service for any amount of data
**KEY EXAM POINTS**: 99.999999999% (11 9's) durability, multiple storage classes, global accessibility
**COMMON EXAM SCENARIO**: "Which service would you use to store website assets?"
```

## 📁 Project Structure

```
aws-cloud-practitioner-chatbot/
├── src/
│   ├── awscloud.py          # Main Streamlit application
│   ├── prompts.py           # Dr. CloudWise system prompt & personality
│   ├── simple_chatbot.py    # Basic chatbot example
│   └── validate_credentials.py  # OpenAI API validation
├── env/                     # Virtual environment (created after setup)
├── .streamlit/
│   └── secrets.toml        # API keys (create this file)
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── LICENSE                # MIT License
```

## 🛠️ Technical Details

- **Frontend**: Streamlit for interactive web interface
- **AI Model**: OpenAI GPT-4o-mini for cost-effective, intelligent responses
- **Streaming**: Real-time response streaming for better UX
- **Session Management**: Streamlit session state for conversation memory
- **Prompt Engineering**: Carefully crafted system prompt for exam focus

## 🎯 Study Strategy Tips

1. **Start with fundamentals**: Begin with cloud concepts before diving into services
2. **Focus on "what" and "why"**: Cloud Practitioner is conceptual, not hands-on
3. **Use the four domains**: Structure your study around exam domains
4. **Practice regularly**: Use the chatbot's practice questions feature
5. **Stay in scope**: Let Dr. CloudWise keep you focused on exam content

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📊 Upcoming Features

- [ ] Progress tracking and study analytics
- [ ] Flashcard generation for key concepts
- [ ] Mock exam simulation mode
- [ ] Study plan recommendations
- [ ] Integration with AWS official resources
- [ ] Offline study materials export

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- AWS for providing comprehensive Cloud Practitioner exam resources
- OpenAI for powerful AI capabilities
- Streamlit for making beautiful web apps simple
- The AWS community for continuous learning support

## 📞 Support

- 📧 **Questions?** Open an issue in this repository
- 💬 **Discussion?** Start a discussion in the Discussions tab
- 🐛 **Bug Report?** Please include steps to reproduce

---

**Ready to ace your AWS Certified Cloud Practitioner exam?** 🚀

Launch the app and start your AI-powered study journey today!
