# Data Science Team Coding Interview Guidelines

This document outlines the evaluation criteria for a coding interview for the Data Science team.

---

## Evaluation Criteria (Part 1)

### **Question 1: Function Description**

**Task:** Describe what the provided function does in 1-2 sentences.

* **Pass:** The candidate understands the function's purpose, which is to convert various data types to a decimal format, and recognizes the exceptions being raised.
* **Fail:** The candidate has no clear understanding of the function's purpose (this is considered very unlikely).

---

### **Question 2: Code Output Prediction**

**Task:** Predict the outputs for the following function calls:
* `to_decimal("100")`
* `to_decimal("")`
* `to_decimal("one")`
* `to_decimal(None)`
* `to_decimal(0.0)`

* **Pass:** The candidate correctly follows the code's execution flow and identifies all the correct outputs.
* **Weak Pass:** The candidate makes 1-2 mistakes in their predictions.
* **Fail:** The candidate makes more than 2 mistakes.

---

### **Question 3: Code Issues Identification**

**Task:** Identify potential issues with the provided code, considering aspects like **type safety**, **error handling**, and **maintainability**.

* **Strong Pass (Builds on Weak Pass):** The candidate identifies issues such as:
    * Duplication of redundant exception handling.
    * Lack of type hinting.
    * An unused `ValueError`.
    * Raising an exception within an exception.
    * The `logger` being imported within an exception block.
* **Weak Pass:** The candidate identifies issues like:
    * Inconsistent return types.
    * The function's handling of non-standard inputs.
* **Fail:** The candidate fails to recognize the inconsistent return type.

---

### **Question 4: Function Refactoring**

**Task:** Rewrite the function to be more robust, based on the issues identified in the previous question, and explain the changes. The candidate will then run unit tests to verify the improved function.

* **Strong Pass (Builds on Weak Pass):** The candidate demonstrates:
    * Explicit handling for each data type.
    * Bundling of exceptions and using an inner conditional.
    * Removal of useless code.
    * Recognition that handling the input `"one"` is not necessary within the time constraints of this question.
* **Weak Pass:** The candidate's refactored function has a consistent return type (decimal).
* **Fail:** The refactored function becomes more complex or fails to pass the unit tests.

---

## Evaluation Criteria (Part 2)

### **Section 2**

**Extra Credit:** The candidate uses `pydantic.field_validator`.

* **Pass:** The candidate recognizes the need to apply `to_decimal` (a manual conversion to a float is also acceptable). The candidate understands the `Participant BaseModel` and its data types.
* **Fail:** The candidate fails to recognize that the issue is due to the input type, is unable to extract information from the classes, or cannot apply the correct conversion (`to_decimal`).

---

### **Section 4**

**Extra Credit:** The candidate uses `pydantic.field_validator`.

* **Pass:** The candidate is familiar with `python-dotenv`, understands the `Participant BaseModel` and its types, and immediately recognizes that `MODEL_TEMPERATURE` will be loaded as a string.
* **Weak Pass:** The candidate can read an `.env` file and understand its relevance to the problem, and they know how to use `os.getenv` or `os.environ`.
* **Fail:** The candidate is unable to understand classes (e.g., `__init__`, attribute setting), cannot get past validation failures, or does not understand how to use an `.env` file (which may indicate a lack of experience with production environments).