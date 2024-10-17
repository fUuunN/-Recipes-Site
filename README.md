# Recipes-Site

This project allows you to quickly and easily search for and view recipes. Users can enter the name of a dish they want to make and see a list of relevant recipes. By clicking on a recipe, they can explore the ingredients and cooking instructions.

## Features

- **Recipe Search**: Enter the name of a dish to see a list of recipes related to that dish.
- **Detailed Recipe View**: When a recipe is selected, the list of ingredients and cooking steps are displayed.
- **Fast Search with Elasticsearch**: Recipes are indexed using Elasticsearch, allowing for quick retrieval of search results.

## Installation

Follow these steps to run the project:

### 1. Clone the Repository

Clone the project files to your computer:

```bash
git clone https://github.com/fUuunN/Recipes-Site.git
cd Recipes-Site
```

### 2. Set Up Elasticsearch

Recipe data is stored and searched using Elasticsearch. You will need to set up your own Elasticsearch installation. You can download it [here](https://www.elastic.co/downloads/elasticsearch).

After installing Elasticsearch, update the connection settings in the `recipe_response` function to connect to your Elasticsearch server.


### 3. Load Recipe Data
You will need to load your data files (for example, guncel_tarifler.json) into Elasticsearch appropriately. This step is not included in the current code. You may create a separate Python script to load your data.

### 4. Start the Application
To run the application, use the following command:

```bash
uvicorn main:app --reload
```

### Usage
- Go to the site
- Enter a dish name in the search bar (for example, "Pizza", "Kebap").
- Relevant recipes will be listed.
- Click on a recipe to view the ingredients and cooking instructions.
### Technologies
- Backend: FastAPI (Python)
- Search Engine: Elasticsearch
- Frontend: HTML, CSS, JavaScript

Happy Cooking! 🍴
