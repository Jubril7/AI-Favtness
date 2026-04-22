"""
Run with: python manage.py shell < seed_data.py
"""
from django.contrib.auth.models import User
from gym.models import Category, PackageType, Trainer, Equipment, Package

# Admin user
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@fitnessfirstng.com', 'admin123')
    print("Superuser created: admin / admin123")

# Categories
cats = ['Weight Training', 'Cardio', 'Yoga & Wellness', 'Group Classes', 'Martial Arts']
cat_objs = {}
for c in cats:
    obj, _ = Category.objects.get_or_create(name=c, defaults={'description': f'{c} focused programs'})
    cat_objs[c] = obj

# Package Types
types = ['Basic', 'Standard', 'Premium', 'VIP']
type_objs = {}
for t in types:
    obj, _ = PackageType.objects.get_or_create(name=t, defaults={'description': f'{t} membership tier'})
    type_objs[t] = obj

# Packages
packages = [
    ('Starter Fitness', 'Weight Training', 'Basic', 1, 49.99),
    ('Monthly Cardio Blast', 'Cardio', 'Standard', 1, 69.99),
    ('Yoga & Mindfulness', 'Yoga & Wellness', 'Standard', 1, 25000),
    ('Full Access Monthly', 'Group Classes', 'Premium', 1, 35000),
    ('Quarterly Power Pack', 'Weight Training', 'Premium', 3, 90000),
    ('6-Month Transformation', 'Group Classes', 'VIP', 6, 165000),
    ('Annual Wellness Pass', 'Yoga & Wellness', 'VIP', 12, 290000),
    ('Kickboxing Monthly', 'Martial Arts', 'Standard', 1, 28000),
]
for name, cat, ptype, duration, price in packages:
    Package.objects.get_or_create(
        name=name,
        defaults={
            'category': cat_objs[cat],
            'package_type': type_objs[ptype],
            'description': f'Our {name} package gives you full access to world-class {cat.lower()} facilities and expert guidance for {duration} month(s).',
            'duration_months': duration,
            'price': price,
        }
    )

# Trainers
trainers = [
    ('Chisom Okafor', 'Strength & Conditioning', 'Certified strength coach from Abuja, passionate about empowering women through fitness.', 8),
    ('Adaeze Nwosu', 'Yoga & Pilates', 'Experienced yoga instructor from Enugu focused on mind-body wellness and inner peace.', 6),
    ('Funmilayo Adeyemi', 'Cardio & HIIT', 'High-energy cardio specialist from Abuja who makes every session fun and results-driven.', 5),
    ('Ngozi Eze', 'Kickboxing & Combat Fitness', 'Former Nigerian kickboxing champion turned trainer — intense, motivating, results-driven.', 7),
    ('Amaka Obiora', 'Nutrition & Wellness', 'Holistic wellness coach from Port Harcourt combining fitness with healthy nutrition habits.', 4),
    ('Tolu Babatunde', 'Personal Training', 'Top personal trainer from Ibadan specialising in body transformation and athletic performance.', 9),
    ('Jubril Bucknor', 'Strength & Athletic Performance', 'Elite strength coach and athlete from Abuja — known for pushing members beyond their limits and delivering real results.', 7),
    ('Favor Chinonso', 'Cardio & Body Transformation', 'Certified fitness coach from Anambra with a passion for body transformation and helping clients build confidence through fitness.', 5),
]
for name, spec, bio, exp in trainers:
    Trainer.objects.get_or_create(name=name, defaults={'specialization': spec, 'bio': bio, 'experience_years': exp})

# Equipment
equipment = [
    ('Treadmill', 'Commercial-grade treadmill with incline settings and heart-rate monitor.', 15),
    ('Dumbbells (5–100 lbs)', 'Full rack of rubber-coated hex dumbbells.', 1),
    ('Smith Machine', 'Heavy-duty Smith machine for guided barbell movements.', 4),
    ('Spin Bikes', 'Magnetic resistance spin bikes for cardio classes.', 20),
    ('Yoga Mats', 'Non-slip premium yoga mats.', 30),
    ('Rowing Machine', 'Air-resistance concept rowing machine.', 8),
    ('Cable Machine', 'Dual adjustable pulley cable machine.', 6),
    ('Leg Press', 'Plate-loaded leg press / hack squat combo.', 3),
    ('Pull-up Rig', 'Multi-grip pull-up and dip station.', 4),
    ('Battle Ropes', 'Heavy-duty battle ropes for conditioning.', 6),
]
for name, desc, qty in equipment:
    Equipment.objects.get_or_create(name=name, defaults={'description': desc, 'quantity': qty})

print("Seed data loaded successfully!")
print("Packages:", Package.objects.count())
print("Trainers:", Trainer.objects.count())
print("Equipment:", Equipment.objects.count())
