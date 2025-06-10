import matplotlib.pyplot as plt


def plot_weekly_temperatures(temperatures, days):
    """
    Plots temperature readings over a week, highlighting the hottest and coldest days.

    Parameters:
        temperatures (list of int): Temperature values for each day.
        days (list of str): Corresponding day names.
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(
        days, temperatures, color='blue', marker='o', linestyle='-', linewidth=2, markersize=8, label='Temperature')

    ax.set_ylim(15, 30)

    fig.suptitle("Weekly Temperature Report", fontsize=16, fontweight='bold')

    ax.set_xlabel("Day of the Week", fontsize=12)
    ax.set_ylabel("Temperature (°C)", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.6)

    max_temp = max(temperatures)
    min_temp = min(temperatures)
    max_day = days[temperatures.index(max_temp)]
    min_day = days[temperatures.index(min_temp)]

    ax.plot(
        max_day, max_temp, marker='o', color='red', markersize=10, label='Hottest Day')

    ax.annotate(
        f'{max_temp}°C', xy=(max_day, max_temp), xytext=(0, 10), textcoords='offset points', ha='center', color='red', fontsize=10)

    ax.plot(
        min_day, min_temp, marker='o', color='cyan', markersize=10, label='Coldest Day')
    ax.annotate(
        f'{min_temp}°C', xy=(min_day, min_temp), xytext=(0, -15), textcoords='offset points', ha='center', color='cyan', fontsize=10)

    ax.legend()

    plt.show()


if __name__ == '__main__':
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    temperatures = [20, 22, 19, 23, 21, 24, 20]

    plot_weekly_temperatures(temperatures, days)
