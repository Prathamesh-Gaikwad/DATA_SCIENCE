import matplotlib.pyplot as plt

subject = ["C", "Data-structure", "C++", "JAVA", "WEB-Technology"]
marks = [96, 99, 96, 98, 94]
colors = ["red", "green", "violet", "blue", "orange"]

plt.pie(marks, labels = subject, colors = colors, autopct = "%1.1f%%", shadow = True)
plt.bar(subject, marks)
plt.title("Subjects And Marks Pie Chart")
plt.show()
