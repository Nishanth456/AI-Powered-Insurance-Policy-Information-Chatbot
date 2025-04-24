# AI-Powered-Insurance-Policy-Information-Chatbot
This project develops an AI-powered chatbot for SBI Home Insurance, providing users with real-time assistance, policy information, and seamless escalation to human agents when needed.

# SBI Home Insurance Chatbot

## Project Overview

This project involves developing an AI-powered chatbot to assist users with queries related to the **SBI Home Insurance Policy**. The chatbot leverages advanced **Natural Language Processing (NLP)** and **Generative AI** techniques to provide accurate and real-time responses to policy-related questions. Additionally, the system integrates an escalation mechanism to redirect users to a human agent when necessary.

## Key Features

- **AI-Powered Assistance**: The chatbot can answer questions about SBI Home Insurance policies.
- **Real-time Chat History**: A memory feature that retains the context of previous interactions to improve the quality of responses.
- **Escalation to Human Agent**: The chatbot automatically triggers a fallback mechanism when it cannot answer certain questions, or when a user shows frustration or needs help.
- **Streamlit Interface**: The chatbot is integrated with a user-friendly **Streamlit** interface for web-based interaction.

## Methodology

### 1. **Data Collection**:
The project uses an existing **SBI Home Insurance PDF document** to extract and structure relevant policy information. The content is indexed into a **vector store** using embeddings for fast and accurate retrieval.

### 2. **Embedding and Vector Search**:
The question asked by the user is converted into an embedding using the `sentence-transformers/all-MiniLM-L6-v2` model, and a **FAISS vector store** is used to store the embeddings of the document. The system performs a similarity search to retrieve the most relevant context for answering the query.

### 3. **Generative AI Model**:
The chatbot uses the **Groq LLaMA-3.3-70B** model to generate answers based on the context retrieved from the vector store. The model is designed to be highly flexible and capable of handling a wide range of insurance-related queries.

### 4. **Fallback Mechanism**:
If the chatbot cannot provide an answer (either due to insufficient information or user frustration), it triggers a fallback mechanism to connect the user to a **human agent** for further assistance.

### 5. **Streamlit Interface**:
The user interacts with the chatbot through a simple, intuitive interface built using **Streamlit**. The interface allows users to type questions, receive real-time answers, and view chat history.

### 6. **Chat History**:
A **chat history** feature is included to keep track of all interactions, which helps both the model and human agents understand the context of the conversation. The chat history is stored in a **JSON file** for persistence across sessions.

## Setup and Installation

To run the chatbot on your local machine, follow the instructions below:

### Prerequisites

- Python 3.x
- `pip` for installing dependencies
- Streamlit
- Groq API key

### Steps to Run the Chatbot

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Nishanth456/sbi-home-insurance-chatbot.git
    cd sbi-home-insurance-chatbot
    ```

2. **Install Dependencies**:
    Use `pip` to install the required Python packages.
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up API Keys**:
    - Sign up for Groq's API and get an API key.
    - Create a `.env` file in the project directory and add your **Groq API Key**:
    ```bash
    GROQ_API_KEY=your_api_key_here
    ```

4. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

    This will start a local server where you can interact with the chatbot in your browser.

## Results

### 1. **Accuracy of Responses**:
The chatbot was able to answer a wide range of questions related to the SBI Home Insurance Policy by utilizing the vector-based search method to retrieve relevant information. 

### 2. **User Experience**:
Through the Streamlit interface, users found the interaction to be intuitive and easy to use. The escalation mechanism worked effectively to connect users with a human agent when needed.

### 3. **Fallback Efficiency**:
The fallback mechanism was able to redirect users to a human agent when the chatbot encountered frustration-related queries or issues that required manual intervention. 

### 4. **Real-time Context**:
By maintaining a chat history, the model could provide context-aware responses, significantly improving user experience over multiple interactions.

## Future Improvements

- **Better NLP Models**: We could upgrade to more powerful language models to handle more complex queries.
- **Personalization**: The chatbot could be personalized by storing user preferences, providing a more tailored experience.
- **Multilingual Support**: Adding support for multiple languages could broaden accessibility for users from different linguistic backgrounds.

## Conclusion

This chatbot solution provides a reliable, scalable way to assist users with their SBI Home Insurance policies. The use of generative AI, vector search, and real-time chat history allows for an interactive and efficient customer support experience. The fallback to human agents ensures that user queries are always addressed, even when the chatbot cannot handle them.

By implementing this solution, the insurance company can improve customer satisfaction and reduce the workload on human agents by automating routine queries.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
