# 🏥 Tecchy Medico

**AI-Powered Medical Image Analysis Platform**

Tecchy Medico is an intelligent medical image analysis application that leverages Google's Gemini AI to provide preliminary insights on medical images. Upload an image, get instant AI-powered analysis to help identify possible conditions and abnormalities.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Google Gemini](https://img.shields.io/badge/Gemini-AI-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [API Key Setup](#-api-key-setup)
- [Disclaimer](#-disclaimer)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- 🔐 **Secure API Key Input** - Password-protected input for your Gemini API key
- 📤 **Easy Image Upload** - Support for PNG, JPG, and JPEG formats
- 🤖 **AI-Powered Analysis** - Leverages Google Gemini AI for medical image interpretation
- 📊 **Detailed Reports** - Comprehensive analysis with findings, recommendations, and next steps
- 💾 **Export Reports** - Download analysis results as text files
- 🎨 **Modern UI** - Clean, intuitive interface built with Streamlit
- ⚡ **Fast Processing** - Quick analysis results in seconds
- 🔒 **Privacy-Focused** - No data storage; all processing happens in real-time

---

## 🎬 Demo

1. Enter your Gemini API key
2. Upload a medical image
3. Click "Analyze"
4. View detailed AI-generated analysis
5. Download the report

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A Google Gemini API key ([Get one here](https://aistudio.google.com/))

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/tecchy-medico.git
   cd tecchy-medico
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (optional)
   ```bash
   # Copy the example env file
   cp .env.example .env

   # Edit .env and add your API key
   GEMINI_API_KEY=your_api_key_here
   MODEL_NAME=gemini-2.0-flash-exp
   ```

5. **Run the application**
   ```bash
   streamlit run app/main.py
   ```

6. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to that URL

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Required (or enter via UI)
GEMINI_API_KEY=your_gemini_api_key_here

# Model Configuration
MODEL_NAME=gemini-2.0-flash-exp
AI_TEMPERATURE=0.4
AI_TOP_P=1.0
AI_TOP_K=32
AI_MAX_TOKENS=4096

# Application Settings
APP_NAME=Tecchy Medico
ENV=production
```

**Note:** If you don't set `GEMINI_API_KEY` in the `.env` file, you can enter it directly in the web interface.

---

## 📖 Usage

### Basic Workflow

1. **Launch the Application**
   ```bash
   streamlit run app/main.py
   ```

2. **Enter API Key**
   - If not set in `.env`, enter your Gemini API key in the input field
   - The key is masked for security (password type input)

3. **Upload Medical Image**
   - Click "Browse files" or drag and drop
   - Supported formats: PNG, JPG, JPEG
   - Maximum file size: 10MB

4. **Generate Analysis**
   - Click the "Analyze Image" button
   - Wait for the AI to process (usually 5-15 seconds)
   - View the comprehensive analysis report

5. **Download Report**
   - Click "Download Report" to save results as a text file
   - Share with healthcare professionals if needed

### Example Analysis Output

The AI provides:
- **Overview**: General description of what's visible in the image
- **Key Observations**: Specific findings and abnormalities
- **Potential Conditions**: Possible diagnoses based on observations
- **Severity Assessment**: Urgency and risk level
- **Recommendations**: Suggested next steps and tests
- **Disclaimer**: Reminder to consult medical professionals

---

## 📁 Project Structure

```
tecchy-medico/
│
├── app/
│   ├── config/
│   │   └── settings.py          # Configuration management
│   │
│   ├── core/
│   │   └── prompt_builder.py    # Medical analysis prompt templates
│   │
│   ├── services/
│   │   ├── ai_service.py        # Abstract AI service interface
│   │   └── gemini_service.py    # Gemini AI implementation
│   │
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── analysis_page.py     # Main analysis interface
│   │   ├── api_input.py         # API key input widget
│   │   ├── css.py               # Custom styling
│   │   ├── download_report.py   # Report download functionality
│   │   ├── footer.py            # Footer component
│   │   ├── get_api.py           # API key help/instructions
│   │   └── uploader.py          # File upload widget
│   │
│   └── main.py                  # Application entry point
│
├── .env                         # Environment variables (create this)
├── .env.example                 # Example environment file
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

### Key Files Explained

- **`main.py`**: Entry point of the application, sets up the Streamlit interface
- **`settings.py`**: Manages configuration and environment variables
- **`prompt_builder.py`**: Contains the medical analysis prompt template for AI
- **`gemini_service.py`**: Handles communication with Google Gemini API
- **`ai_service.py`**: Abstract base class for AI services (enables future expansion)
- **`uploader.py`**: File upload widget with validation
- **`api_input.py`**: Secure API key input with validation

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Web application framework |
| **Google Gemini AI** | AI-powered image analysis |
| **python-dotenv** | Environment variable management |
| **Pillow** | Image processing and validation |

### Dependencies

```txt
streamlit>=1.28.0
python-dotenv>=1.0.0
google-generativeai>=0.3.0
google-genai>=0.2.0
Pillow>=10.0.0
```

---

## 🔑 API Key Setup

### Getting Your Gemini API Key

1. **Visit Google AI Studio**
   - Go to [https://aistudio.google.com/](https://aistudio.google.com/)

2. **Sign In**
   - Use your Google account
   - If you don't have one, create it for free

3. **Create API Key**
   -  Sign in with Google
   -  Click on Dashboard on the left side
   -  Click "Create API Key"  
   -  It will then ask for an imported project to select 
   -  Create a new projet by clicking Create Project
   -  Select your Project
   -  Click "Create Key Button" 

4. **Copy Your Key**
   - Your key will look like: `AIzaSyA...` (39 characters)
   - Click the copy icon
   - Store it securely

5. **Use in Tecchy Medico**
   - **Option 1**: Add to `.env` file as `GEMINI_API_KEY=your_key`
   - **Option 2**: Enter directly in the web interface

### API Key Security

⚠️ **Important Security Notes:**
- ❌ Never commit API keys to Git/GitHub
- ❌ Don't share keys in screenshots or public forums
- ✅ Use `.env` file (add to `.gitignore`)
- ✅ Rotate keys periodically
- ✅ Use environment variables in production

---

## ⚕️ Disclaimer

### Important Medical Notice

**THIS IS NOT A MEDICAL DEVICE OR DIAGNOSTIC TOOL**

Tecchy Medico is an AI-assisted educational and research tool designed to provide preliminary image analysis. It is **NOT** a substitute for professional medical advice, diagnosis, or treatment.

**Please Note:**
- ⚠️ This tool provides AI-generated suggestions only
- ⚠️ Results are NOT clinically validated
- ⚠️ Do NOT use for self-diagnosis or treatment decisions
- ⚠️ Always consult qualified healthcare professionals
- ⚠️ In medical emergencies, seek immediate professional help
- ⚠️ The developers assume no liability for medical decisions made using this tool

**Intended Use:**
- Educational purposes
- Research and exploration
- Learning about AI in healthcare
- Preliminary screening (must be validated by professionals)

**Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.**

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

1. **Report Bugs**
   - Open an issue describing the problem
   - Include steps to reproduce
   - Add screenshots if applicable

2. **Suggest Features**
   - Open an issue with the `enhancement` label
   - Describe the feature and use case
   - Explain why it would be useful

3. **Submit Pull Requests**
   - Fork the repository
   - Create a feature branch (`git checkout -b feature/AmazingFeature`)
   - Commit your changes (`git commit -m 'Add some AmazingFeature'`)
   - Push to the branch (`git push origin feature/AmazingFeature`)
   - Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/tecchy-medico.git
cd tecchy-medico

# Create virtual environment
python -m venv venv
 venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Make your changes
# ...

# Test your changes
streamlit run app/main.py

# Submit PR
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Tecchy Medico

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🆘 Support

### Getting Help

- 📖 **Documentation**: Check this README
- 🐛 **Bug Reports**: [Open an issue](https://github.com/PravasMohanty/Techhy-Medico/issues)
- 💬 **Questions**: [Start a discussion](https://github.com/PravasMohanty/Techhy-Medico/discussions)
- 📧 **Email**: pravasmohanty1000@gmail.com

### Common Issues

**"Invalid API Key" Error**
- Verify key starts with `AIza`
- Check for extra spaces
- Ensure key is from Google AI Studio
- Try creating a new key

**"Quota Exceeded" Error**
- Free tier: 60 requests/minute
- Wait 60 seconds and retry
- Check usage at [ai.google.dev](https://ai.google.dev)

**Image Upload Fails**
- Check file size (max 10MB)
- Verify format (PNG, JPG, JPEG only)
- Try a different image

---



## 🙏 Acknowledgments

- **Google Gemini AI** for providing the AI analysis capabilities
- **Streamlit** for the excellent web framework
- **Open-source community** for inspiration and support
- **Medical professionals** for feedback and guidance


---

<div align="center">

**Made with ❤️ for the healthcare community**

If you found this project helpful, please ⭐ star the repository!

</div>

---

## 📸 Screenshots

### Main Interface
![Main Interface](docs/screenshots/main-interface.png)

### Analysis Result
![Analysis Result](docs/screenshots/analysis-result.png)

### API Key Setup
![API Setup](docs/screenshots/api-setup.png)

---

**Version**: 1.0.0  
**Last Updated**: February 2026  
**Status**: Active Development

---