
import random
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt



#I create picker function, that randomly picks options if we were live in 1912, what would I be
# Parameters are lucky number and list of choice.
# For example Male-Female, Embark Town, Pclass, Deck


def picker(lucky_number=0,choice=[]):
    random.seed(lucky_number)
    global pick
    pick =random.choices(choice,k=1)
    print(pick)


# I  create a generator of survived&death
# In this function there 2 parameters,you write your luckiest number,it will used for random.seed()
# The other parameter is the weight of the probability
# It produces if you would survived or death according to your lucky number and probability.
def survived_death(lucky_number=0,probability=0.5):
    random.seed(lucky_number)
    probability = float(probability)
    deathorsurvived = random.choices([0,1],weights=((1-probability),probability),k=1)

    if deathorsurvived[0] == 1:

        print("You're survived!!")
    else:
        print("You're death!")


def titanic(df, column,lucky_number=0):
    picker(lucky_number, df[column].unique())
    probs = df.groupby(column).agg({"survived": "mean"})
    prob = probs.loc[pick, "survived"]
    print(probs)

    print(f"When u select {column} column with groupby survival,picker function  chose {str(pick).upper()},and the probability of being alive is {float(prob)}")
    print(f"By the chance of {round(float(prob), 2)} :")
    survived_death(lucky_number, prob)

df = sns.load_dataset("titanic")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


df.head()
df.info()
df.describe().T
df= df[["survived","pclass","sex","age","embark_town"]]



for col in df.columns:
    unique_values = df[col].unique()
    unique_values_str = ', '.join(str(value) for value in unique_values)
    print(f"Unique values in column '{col}': {unique_values_str}")

df["age"] = df["age"].fillna(df["age"].median())

df["embark_town"] = df["embark_town"].fillna(df["embark_town"].mode()[0])


df["age_cat"] = pd.qcut(df["age"],4,labels=[1,2,3,4])

df["embark_town"].isnull().sum()


df.isnull().any()

df.isnull().sum()


sns.boxplot(df, x="sex", y="age")
plt.show()


# Probability of Survival according to gender
df.groupby("sex").agg({"survived":["sum","mean","count"]})



titanic(df,"pclass",15)
titanic(df,"sex",60)
titanic(df,"embark_town",13)
titanic(df,"age_cat",5)
