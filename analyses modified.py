import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_planetary_data():
    """Load the planetary data into a Pandas dataframe"""
    data = {
        'Planet/Moon': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Moon', 'Europa', 'Enceladus', 'Titan'],
        'Diameter (km)': [4879, 12104, 12756, 6792, 142984, 116460, 50724, 49528, 3475, 4879, 504, 5150],
        'Mass (kg)': [3.3022e23, 4.8695e24, 5.9723e24, 6.4171e23, 1.8986e27, 5.6846e26, 8.6810e25, 1.0243e26, 7.349e22, 4.879e22, 1.08e23, 1.89e23],
        'Orbital Period (days)': [87.969, 224.701, 365.256, 687.024, 4332.820, 10759.220, 30687.150, 60190.030, 27.3217, 3.156, 1.37, 15.945],
        'Surface Temperature (K)': [173, 737, 288, 210, 124, 95, 59, 48, 100, 103, 95, 94],
        'Atmosphere': ['Thin', 'Thick', 'Moderate', 'Thin', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'Hydrogen', 'None', 'Thin', 'Thin', 'Thick'],
        'Moons': [0, 0, 1, 2, 79, 62, 27, 14, 0, 0, 0, 0],
        'Habitability Score': [0.1, 0.2, 0.8, 0.4, 0.01, 0.05, 0.1, 0.05, 0.3, 0.6, 0.7, 0.4]
    }
    return pd.DataFrame(data)

def calculate_habitability_scores(df):
    """Calculate habitability scores based on planetary attributes"""
    def habitability_score(row):
        score = 0
        if row['Surface Temperature (K)'] > 250 and row['Surface Temperature (K)'] < 300:
            score += 0.2
        if row['Atmosphere'] == 'Moderate':
            score += 0.3
        if row['Moons'] > 0:
            score += 0.1
        return score

    df['Habitability Score'] = df.apply(habitability_score, axis=1)
    return df

def visualize_habitability_scores(df):
    """Visualize the habitability scores"""
    sns.set()
    sns.barplot(x='Planet/Moon', y='Habitability Score', data=df)
    plt.xlabel('Planet/Moon')
    plt.ylabel('Habitability Score')
    plt.title('Barplot of Habitability Scores')
    plt.show()

def visualize_correlation_matrix(df):
    """Visualize the correlation matrix between planetary attributes"""
    corr_matrix = df[['Diameter (km)', 'Mass (kg)', 'Orbital Period (days)', 'Surface Temperature (K)', 'Habitability Score']].corr()
    sns.set()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title('Heatmap of Correlation Matrix')
    plt.show()

if __name__ == '__main__':
    df = load_planetary_data()
    df = calculate_habitability_scores(df)
    visualize_habitability_scores(df)
    visualize_correlation_matrix(df)
    #این کد به تجزیه داده ها برای پی بردن به زندگی در سشیارات و قمرهاست