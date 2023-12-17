# Itinerary Planning - Machine Learning
Bangkit 2023 Batch 2 Product-based Capstone

##  Machine Learning Members
| Bangkit ID | Name | University |
|-----|-------|------|
| M643BSX0286   | Theophanie Scholastica Tanzil |  Institut Bio Scientia Internasional Indonesia |
| M247BSY0198   |  Muhammad Bashir Hanafi  | Universitas Lambung Mangkurat | 
| M010BSX1109 | Safira Aulia | Universitas Indonesia |

# Dataset
The attractions dataset is sourced from [GetLoc](https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destination) and from [OutScrapping](https://app.outscraper.com/tasks) tools. The images of attractions is sourced from Google Images and we're crawling this dataset using BeautifulSoup library in Python.

We've opened the clean dataset to the public, allowing access through our Kaggle dataset.

# Machine Learning Models
## 1. Multi-armed Bandit
A multi-armed Bandit is scenario when a person needs to make sequential decisions while facing uncertainty about which actions will yield the best overall rewards and trying to maximize its reward by selecting from multiple options (or 'arms'). Thompson Sampling is a probabilistic algorithm used in the field of reinforcement learning for balancing the exploration-exploitation trade-off.

Our application employs the Thompson Sampling approach to dynamically select keywords for recommending to users, leveraging the uncertainty of choices to optimize recommendations and maximize user satisfaction.

## 2. Itinerary Planning
### a. Generate New Preference
Word2Vec is a neural network-based algorithm that learns word embeddings, which are numerical representations of words that capture semantic and syntactic relationship. The Continous Bag of Words (CBOW) model is method for training word embeddings, which are predict a target word given the context word in a sentence.

Our application employs this approach to generate new preference based on the user's input attraction preferences. For instance, when the user inputs 'wisata' + 'air', the result will be the summation of preferences, wherein Word2Vec will yield 'pantai', so the user preferences will be 'wisata', 'air', and 'pantai'.

### b. Content-based Filtering
Content-based filtering is recommender systems leverages machine learning algorithms to predict and recommend new but similar items to the user. Text vectorization is approach to determining how similar two texts are, which will convert input texts into vectors (embeddings) that capture semantic information and calculate how close (similar) they are between them.

Our application uses a content-based filtering approach leveraging text similarity using TF-IDF word embbeding to recommend items based on user preferences. This approach helps in continuing the process of suggesting relevant items tailored to each user's interests.
### c. Filtering
#### 1. Rating Exploitation and Exploration
Beside leveraging the uncertainty of keyword choices on the recommender system, Thompson Sampling is utilized for rating exploitation and exploration. In this method, the best rating will be determined through a balance between exploring new possibilities and exploiting the current best-known options.
#### 2. Budget Optimization
A greedy algorithm is an approach for solving a problem by make each step as it attempts to find the optimal way to solve the entire problem. This algorithm can be applied to solve any optimization problem requires maximuum or minimum result. Our application using this algorithm to optimization the budget based on the input of user.
#### 3. Duration Filtering
After optimizing the user's budget, our application employs duration filtering to refine the selection of options based on the optimized budget. We just using simple duration filtering with the result of optimized budget.
#### 4. Traveling Salesman Problem
Traveling Salesman Problem (TSP) is about finding the best route to reach a given destination given a set of specific destinations. TSP tried to answer the question about which shortest route the salesperson had to take so that only visited each location once before returning to the starting point. TSP can be optimized with Nearest Neighbors, which is start an one location and repeatedly select the nearest unvisited location until all location have been visited. Our application using Traveling Salesman Problem approach to optimization the attractions and helping user to visited each one before returning to the user starting point.
## 3. Carbon Footprint Prediction

# Deployment

# Tools

# References
