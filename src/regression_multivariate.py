import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv('StudentPerformanceFactors.csv')

X = df[['Hours_Studied', 'Attendance']]
y = df['Exam_Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))

hours_studied = X_test["Hours_Studied"]
attendance = X_test["Attendance"]
attendance_range = np.linspace(attendance.min(), attendance.max(), 10)
hours_range = np.linspace(hours_studied.min(), hours_studied.max(), 10)
attendance_range, hours_range = np.meshgrid(attendance_range, hours_range)
predicted_scores = model.intercept_ + model.coef_[0] * hours_range + model.coef_[1] * attendance_range
fig = plt.figure(figsize = (10, 8))
ax = fig.add_subplot(111, projection = "3d")
ax.scatter(attendance, hours_studied, y_test, color = "blue", label = "Actual_Data", alpha = 0.5)
ax.plot_surface(attendance_range, hours_range, predicted_scores, color = "red", alpha = 0.5)
ax.set_xlabel("Attendance")
ax.set_ylabel("Hours Studied")
ax.set_zlabel("Exam Score")
plt.title("3D Regression Plane : Attendance and Hours Studieds vs Exam Score")
plt.show()
