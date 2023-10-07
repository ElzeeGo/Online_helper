# Chat GPT Extension User Manual

## Introduction

The Chat GPT Extension is a Google Chrome extension that allows users to call out the Chat GPT-4 model in text fields on websites. By pressing a key binding (e.g., Alt + N), users can activate Chat GPT-4 for a specific text space and start generating AI-powered responses.

This user manual provides detailed instructions on how to install the extension, configure the necessary dependencies, and use the Chat GPT Extension effectively.

## Installation

To install the Chat GPT Extension, follow these steps:

1. Download the extension files from the provided source.
2. Open Google Chrome and go to the Extensions page by entering `chrome://extensions` in the address bar.
3. Enable the "Developer mode" toggle switch located at the top right corner of the Extensions page.
4. Click on the "Load unpacked" button and select the folder containing the extension files.
5. The Chat GPT Extension should now be installed and visible in the Extensions list.

## Configuration

Before using the Chat GPT Extension, you need to configure the necessary dependencies. Follow these steps to set up the environment:

1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt and navigate to the folder containing the extension files.
3. Install the required Python dependencies by running the following command: `pip install -r requirements.txt`
4. Replace the placeholder `YOUR_API_KEY` in the `main.py` file with your actual OpenAI API key.

## Usage

Once the Chat GPT Extension is installed and configured, you can start using it to generate AI-powered responses in text fields on websites. Follow these steps to use the extension:

1. Open Google Chrome and navigate to a website with a text field where you want to activate Chat GPT-4.
2. Click on the text field to make it active or use the keyboard to navigate to the desired text field.
3. Press the key binding Alt + N to activate Chat GPT-4 for the selected text field.
4. A prompt will be generated, and the extension will send it to the Chat GPT-4 API for processing.
5. The AI-generated response will be displayed in a pop-up window.

## Limitations

Please note the following limitations of the Chat GPT Extension:

- The extension currently supports manifest version 3 and uses the background.service_worker key.
- The extension requires an active internet connection to communicate with the OpenAI Chat GPT-4 API.
- The extension may not work correctly on websites with complex JavaScript interactions or security restrictions.
- The extension is designed for text fields where text input is possible. It may not work as expected on other types of input fields.

## Troubleshooting

If you encounter any issues while using the Chat GPT Extension, try the following troubleshooting steps:

1. Ensure that you have a stable internet connection.
2. Verify that your OpenAI API key is correctly configured in the `main.py` file.
3. Check if there are any error messages in the browser console (press F12 to open the Developer Tools).
4. Disable any conflicting extensions or browser settings that may interfere with the Chat GPT Extension.
5. If the issue persists, contact the support team for further assistance.

## Conclusion

The Chat GPT Extension provides a convenient way to leverage the power of the Chat GPT-4 model in text fields on websites. By following the installation and usage instructions in this user manual, you can enhance your browsing experience and generate AI-powered responses effortlessly. Enjoy using the Chat GPT Extension!