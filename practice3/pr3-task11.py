import matplotlib.pyplot as plt


def parse_data():
    years = {str(x): 0 for x in range(1981, 2005)}
    genres = {}
    with open('games.csv', encoding='utf8') as file:
        for line in file:
            data = [x.strip('\"') for x in line.replace('\n', '').split(';')]
            name, genre, link, year = data

            # number of games per year
            if not year.isdecimal():
                continue
            if years.get(year) is not None:
                years[year] += 1

            # number of games each year per genre
            if genres.get(genre) is None:
                genres[genre] = {str(x): 0 for x in range(1981, 2005)}
            else:
                if genres[genre].get(year) is not None:
                    genres[genre][year] += 1

    return years, genres


def main():
    # general plot settings
    years, genres = parse_data()
    font1 = {'family': 'serif', 'size': 20}
    font2 = {'family': 'serif', 'size': 15}

    # years plot settings
    plt.figure(figsize=(16, 4.8))
    plt.grid(axis='y', linestyle='--')
    plt.title("Games released by year", fontdict=font1)
    plt.xlabel("Year", fontdict=font2)
    plt.ylabel("Games", fontdict=font2)

    # years plot making
    plt.bar(years.keys(), years.values())
    plt.savefig('images/plot_years', bbox_inches='tight')
    plt.close()

    # genres plot settings
    plt.figure(figsize=(16, 4.8))
    plt.grid(axis='x', linestyle='--')
    plt.title("Popularity of genres", fontdict=font1)
    plt.xlabel("Year", fontdict=font2)
    plt.ylabel("Games", fontdict=font2)

    # genres plot making
    for genre in genres:
        plt.plot(genres[genre].keys(), genres[genre].values(), label=genre)
    plt.legend()
    plt.savefig('images/plot_genres', bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    main()
