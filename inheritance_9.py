'''
9. Inheritence
1. Create inheritance using MobilePhone as base class and Apple &
Samsung as child class
1. The base class should have properties:
1. ScreenType = Touch Screen
2. NetworkType = 4G/5G
3. DualSim = True or False
4. FrontCamera = (5MP/8MP/12MP/16MP)
5. rearCamera = (8MP/12MP/16MP/32MP/48MP)
6. RAM = (2GB/3GB/4GB)
7. Storage = (16GB/32GB/64GB)
2. Create basic mobile phone functionalities in the classes like:
make_call, recieve_call, take_a_picture, etc.
3. Use super() constructor for calling parent class’s constructor
4. Make some objects of Apple class with different properties
5. Make some objects of Samsung class with different properties
'''
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage
    
    def make_call(self, number):
        return f"Making a call to {number}"
    
    def receive_call(self, number):
        return f"Receiving a call from {number}"
    
    def take_a_picture(self):
        return f"Taking a picture with {self.rear_camera} rear camera"

class Apple(MobilePhone):
    def __init__(self, model, screen_type='Touch Screen', network_type='4G/5G', dual_sim=False, front_camera='12MP', rear_camera='48MP', ram='4GB', storage='64GB'):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model
    
    def get_model_info(self):
        return f"Apple {self.model} - Screen Type: {self.screen_type}, Network Type: {self.network_type}, Dual SIM: {self.dual_sim}, 
    Front Camera: {self.front_camera}, Rear Camera: {self.rear_camera}, RAM: {self.ram}, Storage: {self.storage}"

class Samsung(MobilePhone):
    def __init__(self, model, screen_type='Touch Screen', network_type='4G/5G', dual_sim=True, front_camera='16MP', rear_camera='32MP', ram='3GB', storage='32GB'):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model
    
    def get_model_info(self):
        return f"Samsung {self.model} - Screen Type: {self.screen_type}, Network Type: {self.network_type}, Dual SIM: {self.dual_sim}, 
    Front Camera: {self.front_camera}, Rear Camera: {self.rear_camera}, RAM: {self.ram}, Storage: {self.storage}"

apple_phone1 = Apple(model='iPhone 14', front_camera='12MP', rear_camera='48MP', ram='6GB', storage='128GB')
apple_phone2 = Apple(model='iPhone 13', front_camera='12MP', rear_camera='32MP', ram='4GB', storage='64GB')

samsung_phone1 = Samsung(model='Galaxy S21', front_camera='10MP', rear_camera='64MP', ram='8GB', storage='128GB')
samsung_phone2 = Samsung(model='Galaxy A52', front_camera='32MP', rear_camera='64MP', ram='6GB', storage='128GB')
for phone in [apple_phone1, apple_phone2, samsung_phone1, samsung_phone2]:
    print(phone.get_model_info())
    print(phone.make_call('123-456-7890'))
    print(phone.receive_call('098-765-4321'))
    print(phone.take_a_picture())
    print()
