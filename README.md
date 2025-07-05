# 📚 Study Crew V2: Your AI-Powered Study Assistant

![Study Crew](https://img.shields.io/badge/Study%20Crew%20V2-Ready-brightgreen)

Welcome to **Study Crew V2**! This project is designed to enhance your study experience using the power of AI. By leveraging CrewAI, our tool extracts text from PDFs and generates structured summaries and notes, making your learning process more efficient and organized.

## 🚀 Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)
9. [Releases](#releases)

## 🌟 Features

- **AI-Powered Summaries**: Quickly generate concise summaries from lengthy PDFs.
- **Modular Design**: Easily add or modify tasks and tools with our agent-based architecture.
- **YAML Configuration**: Customize your study tasks with simple YAML files.
- **Multi-Format Support**: Extract text from various PDF formats for versatile usage.
- **User-Friendly Interface**: Designed for ease of use, even for those new to AI tools.

## 🛠️ Getting Started

To get started with Study Crew V2, you will need to follow a few simple steps to set up your environment. This will ensure that you can run the application smoothly and take full advantage of its features.

### 📦 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/siunhan284/study-crew-v2.git
   cd study-crew-v2
   ```

2. **Install Dependencies**:
   Use Poetry to manage your dependencies. If you don't have Poetry installed, you can install it by following the instructions [here](https://python-poetry.org/docs/#installation).

   Once you have Poetry installed, run:
   ```bash
   poetry install
   ```

3. **Set Up Your Environment**:
   Make sure to set up your environment variables for the OpenAI API. You can do this by creating a `.env` file in the root of the project:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

### ⚙️ Usage

To run Study Crew V2, you can use the following command:

```bash
poetry run python main.py
```

Once the application is running, you can input your PDF file and specify the output format for the summary. The AI will process the document and provide you with structured notes.

### 📝 Configuration

Study Crew V2 uses YAML files for configuration. You can customize the tasks and tools by editing the `config.yaml` file located in the `config` directory. Here’s an example of how to structure your YAML file:

```yaml
tasks:
  - name: extract_text
    tool: pdf_extractor
    parameters:
      input_file: "path/to/your/file.pdf"
      output_format: "summary"
```

Feel free to modify the parameters according to your needs.

## 🤝 Contributing

We welcome contributions to Study Crew V2! If you have ideas for improvements or want to report issues, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and create a pull request.

Please ensure your code follows the existing style and includes appropriate tests.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 📬 Contact

For any questions or feedback, feel free to reach out to the project maintainer:

- **Name**: Siun Han
- **Email**: siunhan@example.com

## 📦 Releases

To download the latest version of Study Crew V2, visit our [Releases](https://github.com/siunhan284/study-crew-v2/releases) section. Here you will find the necessary files to download and execute.

If you encounter any issues or have questions, check the "Releases" section for updates and fixes.

## 🎨 Technologies Used

- **CrewAI**: The backbone of our AI capabilities.
- **LangChain**: For language model integrations.
- **OpenAI API**: Provides access to powerful language models.
- **Python**: The primary programming language used in this project.
- **Poetry**: Dependency management tool for Python.

## 📊 Project Structure

The project is organized into several directories for clarity:

```
study-crew-v2/
├── config/
│   └── config.yaml
├── src/
│   ├── main.py
│   ├── pdf_extractor.py
│   └── summary_generator.py
├── tests/
│   └── test_summary_generator.py
└── README.md
```

## 🎉 Acknowledgments

We would like to thank the open-source community for their contributions and support. Special thanks to the developers of CrewAI and LangChain for providing the tools that made this project possible.

## 📖 Additional Resources

For more information on AI and automation, consider exploring the following resources:

- [OpenAI Documentation](https://beta.openai.com/docs/)
- [LangChain Documentation](https://langchain.readthedocs.io/en/latest/)
- [YAML Syntax Guide](https://yaml.org/start.html)

## 🔗 Links

- GitHub Repository: [Study Crew V2](https://github.com/siunhan284/study-crew-v2)
- Releases: [Download Latest Version](https://github.com/siunhan284/study-crew-v2/releases)

Thank you for checking out Study Crew V2! We hope it enhances your study experience.