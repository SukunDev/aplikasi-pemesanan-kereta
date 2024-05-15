from models.user_model import UserModel


user_model = UserModel()

print(user_model.get_all_user_schedule(booking_date = 'May, 15 2024'))