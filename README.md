
# Token Count

This project demonstrates how to use OpenAI's GPT model to process a list of strings and return valid English words using the API. The project also tracks the number of tokens used during the API request.

---

## 🛠️ **Technology Stack**

- **Python 3.x**: The programming language used for the implementation.
- **httpx**: A modern Python HTTP client used to send requests to the OpenAI API.
- **OpenAI API**: A service that provides access to the GPT models for text processing.

---

## 📁 **Project Structure**

```
/token-count-api
│
├── main.py       # Main Python script to interact with the OpenAI API and track tokens
├── requirements.txt     # Python dependencies for the project
├── LICENSE              # License file for the project
├── README.md            # This documentation file
```

---

## 🛠️ **How to Run Locally**

1. **Clone the repository** (or copy the code) to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**:
   ```bash
   python token_count.py
   ```

   This will send a request to OpenAI’s API with a predefined list of strings, asking for valid English words. It will also print the number of tokens used during the request.

---

## 🌐 **API Integration**

This project integrates with OpenAI’s API to process messages and return valid English words. The script constructs a JSON payload and sends a POST request to the endpoint using the `httpx` library.

### API Request Details:
- **Endpoint**: `https://api.openai.com/v1/chat/completions`
- **Model**: `gpt-4o-mini`
- **Request Format**: A list of strings passed as the content of the message, with the goal of extracting valid English words.

### Example Request:
```python
{
    "role": "user",
    "content": "List only the valid English words from these: y5W1djP1, eQ0GWWg, rhVr, ffXzPDs, zTkSH8Sb, JaKjT5"
}
```

### Response Example:
```json
{
    "usage": {
        "total_tokens": 20
    }
}
```

---

## 🧑‍💻 **Example Output**

Running the script will print the following output:

```
Number of tokens: 20
```

This output shows the number of tokens consumed by the API request, which is useful for tracking usage and costs.

---

## 📈 **License**

This project is licensed under the MIT License.

---

## 🧑‍💻 **Contributing**

Feel free to open issues or create pull requests if you'd like to contribute to this project!

---

## 📞 **Contact**

For any questions or feedback, feel free to reach out.

---

### **Project Structure Recap**

```
/token-count-api
│
├── token_count.py       # Main Python script to interact with the OpenAI API and track tokens
├── requirements.txt     # Python dependencies for the project
├── LICENSE              # License file for the project
├── README.md            # This documentation file
```

---

### **requirements.txt**

```
httpx==0.23.0
```
