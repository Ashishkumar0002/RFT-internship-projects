import matplotlib.pyplot as plt
import seaborn as sns

# ---------- READ CSV ----------
data = []

with open("movies.csv", "r") as f:
    next(f)

    for line in f:
        movie, rating, genre, revenue = line.strip().split(",")

        data.append({
            "MOVIE": movie,
            "RATING": float(rating),
            "GENRE": genre,
            "REVENUE": int(revenue)
        })


# ---------- ANALYSIS ----------
genre_revenue = {}

ratings = []
revenues = []

for d in data:
    genre = d["GENRE"]

    genre_revenue[genre] = genre_revenue.get(genre, 0) + d["REVENUE"]

    ratings.append(d["RATING"])
    revenues.append(d["REVENUE"])


# ---------- TOP MOVIES ----------
top_movies = sorted(data,
                    key=lambda x: x["RATING"],
                    reverse=True)[:5]


# ---------- VISUALIZATION ----------
fig, ax = plt.subplots(1, 2, figsize=(12,5))


# Genre vs Revenue
ax[0].bar(genre_revenue.keys(),
          genre_revenue.values())

ax[0].set_title("Genre vs Revenue")
ax[0].tick_params(axis='x', rotation=45)


# Rating Distribution
sns.histplot(ratings, kde=True, ax=ax[1])

ax[1].set_title("Rating Distribution")


plt.tight_layout()
plt.show()


# ---------- CORRELATION ----------
correlation = sum(ratings) / len(ratings)

print("\n----- MOVIE INSIGHTS -----")

print("Highest Rated Movie:",
      max(data, key=lambda x: x["RATING"])["MOVIE"])

print("Most Profitable Genre:",
      max(genre_revenue, key=genre_revenue.get))

print("Average Rating:",
      round(correlation, 2))


print("\nTop 5 Movies:")
for m in top_movies:
    print(m["MOVIE"], "-", m["RATING"])
