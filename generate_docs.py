"""
Run: python3 generate_docs.py
Generates: Fitness_First_Project_Report.pdf
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import ListFlowable, ListItem

# ── Colours ──────────────────────────────────────────────────────────────────
PINK     = colors.HexColor('#d4506a')
ROSE     = colors.HexColor('#f9e4e8')
DARK     = colors.HexColor('#2d2d2d')
GRAY     = colors.HexColor('#666666')
LGRAY    = colors.HexColor('#f5f5f5')
WHITE    = colors.white

W, H = A4

# ── Styles ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def style(name, **kw):
    s = ParagraphStyle(name, **kw)
    return s

Title     = style('Title2',    fontSize=26, textColor=PINK,  fontName='Helvetica-Bold', alignment=TA_CENTER, spaceAfter=6)
SubTitle  = style('SubTitle2', fontSize=12, textColor=GRAY,  fontName='Helvetica',      alignment=TA_CENTER, spaceAfter=4)
CoverInfo = style('CoverInfo', fontSize=10, textColor=DARK,  fontName='Helvetica',      alignment=TA_CENTER, spaceAfter=4)
H1        = style('H1',        fontSize=14, textColor=PINK,  fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=4)
H2        = style('H2',        fontSize=11, textColor=DARK,  fontName='Helvetica-Bold', spaceBefore=8,  spaceAfter=3)
Body      = style('Body2',     fontSize=9,  textColor=DARK,  fontName='Helvetica',      leading=14, spaceAfter=4, alignment=TA_JUSTIFY)
Code      = style('Code2',     fontSize=8,  textColor=colors.HexColor('#333'), fontName='Courier',
                  backColor=LGRAY, leftIndent=10, rightIndent=10, spaceBefore=4, spaceAfter=4, leading=12)
Bold      = style('Bold2',     fontSize=9,  textColor=DARK,  fontName='Helvetica-Bold', spaceAfter=2)
Small     = style('Small2',    fontSize=8,  textColor=GRAY,  fontName='Helvetica',      spaceAfter=2)
Center    = style('Center2',   fontSize=9,  textColor=DARK,  fontName='Helvetica',      alignment=TA_CENTER)

def divider():
    return HRFlowable(width='100%', thickness=1, color=ROSE, spaceAfter=8, spaceBefore=4)

def section(title):
    return [Paragraph(title, H1), divider()]

def sub(title):
    return Paragraph(title, H2)

def body(text):
    return Paragraph(text, Body)

def sp(h=6):
    return Spacer(1, h)

def bullet_list(items):
    return ListFlowable(
        [ListItem(Paragraph(i, Body), bulletColor=PINK, leftIndent=14) for i in items],
        bulletType='bullet', bulletFontSize=8, leftIndent=16, spaceAfter=4
    )

# ── Table helpers ─────────────────────────────────────────────────────────────
def plain_table(data, col_widths, header=True):
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    style_cmds = [
        ('FONTNAME',    (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE',    (0,0), (-1,-1), 8),
        ('TEXTCOLOR',   (0,0), (-1,-1), DARK),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [WHITE, LGRAY]),
        ('GRID',        (0,0), (-1,-1), 0.4, colors.HexColor('#e0e0e0')),
        ('VALIGN',      (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING',  (0,0), (-1,-1), 5),
        ('BOTTOMPADDING',(0,0),(-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
    ]
    if header:
        style_cmds += [
            ('BACKGROUND', (0,0), (-1,0), PINK),
            ('TEXTCOLOR',  (0,0), (-1,0), WHITE),
            ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
        ]
    t.setStyle(TableStyle(style_cmds))
    return t

# ── Page numbering ────────────────────────────────────────────────────────────
def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(GRAY)
    canvas.drawCentredString(W / 2, 1.5 * cm, f'Fitness First GYM Management System  |  Page {doc.page}')
    canvas.setStrokeColor(ROSE)
    canvas.setLineWidth(0.5)
    canvas.line(2*cm, 1.9*cm, W-2*cm, 1.9*cm)
    canvas.restoreState()

# ── Build PDF ─────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    'Fitness_First_Project_Report.pdf',
    pagesize=A4,
    leftMargin=2.2*cm, rightMargin=2.2*cm,
    topMargin=2*cm,    bottomMargin=2.5*cm,
)

story = []
TW = W - 4.4*cm   # text width

# ══════════════════════════════════════════════════════════════════
# PAGE 1 — COVER
# ══════════════════════════════════════════════════════════════════
story += [
    sp(50),
    Paragraph('FITNESS FIRST', Title),
    Paragraph('GYM Management System', SubTitle),
    sp(6),
    HRFlowable(width='60%', thickness=2, color=PINK, spaceAfter=16, hAlign='CENTER'),
    sp(10),
    Paragraph('Project Report', style('PR', fontSize=16, textColor=DARK, fontName='Helvetica-Bold', alignment=TA_CENTER, spaceAfter=6)),
    sp(18),
    Paragraph('Developed &amp; Submitted by:', CoverInfo),
    Paragraph('<b>Favor Chinonso</b>', style('CN', fontSize=14, textColor=PINK, fontName='Helvetica-Bold', alignment=TA_CENTER, spaceAfter=4)),
    sp(6),
    HRFlowable(width='30%', thickness=0.5, color=ROSE, spaceAfter=10, hAlign='CENTER'),
    Paragraph('Project Mentor &amp; Supervisor:', CoverInfo),
    Paragraph('<b>Jubril Bucknor</b>', style('JB', fontSize=11, textColor=DARK, fontName='Helvetica-Bold', alignment=TA_CENTER, spaceAfter=2)),
    Paragraph(
        '<i>Mentored project flow, reviewed system architecture,\nand provided technical guidance throughout development.</i>',
        style('JBNote', fontSize=9, textColor=GRAY, fontName='Helvetica-Oblique', alignment=TA_CENTER, spaceAfter=4)
    ),
    sp(16),
    Paragraph('Technology: Python / Django 6.0 &nbsp;&nbsp;|&nbsp;&nbsp; Database: SQLite', CoverInfo),
    Paragraph('Location: Abuja, Nigeria &nbsp;&nbsp;|&nbsp;&nbsp; 2024 / 2025 Academic Session', CoverInfo),
    sp(30),
    HRFlowable(width='100%', thickness=0.5, color=ROSE, spaceAfter=8),
    Paragraph('Fitness First GYM &nbsp;•&nbsp; 14 Ademola Adetokunbo Crescent, Wuse 2, Abuja &nbsp;•&nbsp; hello@fitnessfirstng.com', Small),
    PageBreak(),
]

# ══════════════════════════════════════════════════════════════════
# PAGE 2 — ACKNOWLEDGEMENTS + SYNOPSIS
# ══════════════════════════════════════════════════════════════════
story += section('1. Acknowledgements')
story += [
    body('I, <b>Favor Chinonso</b>, would like to express my deepest gratitude to everyone who played a role — '
         'big or small — in making this project a reality.'),
    sp(4),
    body('First and foremost, I want to give special recognition to <b>Jubril Bucknor</b>, whose mentorship was '
         'invaluable throughout this project. Jubril guided the overall project flow, reviewed the system '
         'architecture, provided technical direction at critical stages, and ensured the project remained '
         'on track from concept to delivery. His support and expertise made a significant difference, '
         'and I am truly grateful for his time and dedication.'),
    sp(4),
    body('I also extend my sincere thanks to my lecturers and academic supervisors for their guidance '
         'and constructive feedback, to my classmates for their encouragement and peer support, '
         'and to my family for their patience and constant motivation throughout this academic session.'),
    body('Finally, I acknowledge the open-source communities behind Django, Bootstrap, and ReportLab — '
         'whose tools formed the foundation of this work.'),
    sp(8),
]

story += section('2. Project Synopsis')
story += [
    sub('Overview'),
    body('Fitness First GYM is a web-based Gym Management System developed by <b>Favor Chinonso</b> '
         'under the mentorship and technical guidance of <b>Jubril Bucknor</b>. '
         'Built using the Python Django framework, the system is designed to replace manual record-keeping '
         'at Fitness First GYM, located in Wuse 2, Abuja. '
         'It provides a fully functional online platform for gym members and administrators.'),
    sp(4),
    sub('Objectives'),
    bullet_list([
        'Allow guest users to explore gym information, packages, trainers, and equipment.',
        'Enable members to register, log in, book packages, and track payment history.',
        'Provide administrators with a dashboard to manage bookings, categories, packages, and generate reports.',
        'Replace manual paper-based processes with a fast, reliable digital system.',
    ]),
    sp(4),
    sub('Technology Stack'),
    plain_table(
        [['Component', 'Technology'],
         ['Backend Framework', 'Python 3.14 / Django 6.0'],
         ['Frontend', 'HTML5, CSS3, Bootstrap 5.3'],
         ['Database', 'SQLite (development)'],
         ['Styling', 'Custom CSS — Poppins + Playfair Display fonts'],
         ['PDF Generation', 'ReportLab 4.x'],
         ['Server', 'Django Development Server'],],
        [TW*0.4, TW*0.6],
    ),
    PageBreak(),
]

# ══════════════════════════════════════════════════════════════════
# PAGE 3 — ANALYSIS + DESIGN
# ══════════════════════════════════════════════════════════════════
story += section('3. Project Analysis')
story += [
    sub('System Modules'),
    plain_table(
        [['Module', 'Users', 'Key Features'],
         ['Guest',    'Public',  'View homepage, packages, trainers, equipment, contact form'],
         ['Member',   'Registered', 'Register/Login, book packages, view payment history, update profile, change password'],
         ['Admin',    'Superuser',  'Dashboard overview, manage categories/packages/package types, update booking payments, view inquiries'],],
        [TW*0.22, TW*0.22, TW*0.56],
    ),
    sp(6),
    sub('Functional Requirements'),
    bullet_list([
        'One-time registration with username, email, and password.',
        'Secure login / logout with session management.',
        'Package booking that auto-calculates start and end dates.',
        'Payment tracking — Pending, Partial, Full statuses.',
        'Admin can update amount paid against any booking.',
        'Contact inquiry form stored in database for admin review.',
        'Category and package-type filters on the packages listing page.',
    ]),
    sp(6),
]

story += section('4. Project Design')
story += [
    sub('4.1  Data Flow (DFD — Level 0)'),
    body('The system has three external entities: <b>Guest User</b>, <b>Registered Member</b>, and <b>Admin</b>. '
         'Data flows from users through the Django view layer into the SQLite database and back as rendered HTML responses.'),
    sp(4),
]

# Simple DFD-style diagram using a table
dfd = Table(
    [
        ['', 'Guest User',         '',  '',            ''],
        ['', '↓ Browse / Inquire', '',  '',            ''],
        ['', 'Django Views',       '←→','SQLite DB',  ''],
        ['', '↑ Register/Book',    '',  '',            ''],
        ['', 'Member / Admin',     '',  '',            ''],
    ],
    colWidths=[TW*0.1, TW*0.3, TW*0.1, TW*0.3, TW*0.2],
)
dfd.setStyle(TableStyle([
    ('FONTNAME',    (0,0),(-1,-1),'Helvetica'),
    ('FONTSIZE',    (0,0),(-1,-1), 9),
    ('ALIGN',       (0,0),(-1,-1),'CENTER'),
    ('VALIGN',      (0,0),(-1,-1),'MIDDLE'),
    ('TEXTCOLOR',   (1,2),(1,2),   PINK),
    ('TEXTCOLOR',   (3,2),(3,2),   colors.HexColor('#1565c0')),
    ('FONTNAME',    (1,2),(1,2),   'Helvetica-Bold'),
    ('FONTNAME',    (3,2),(3,2),   'Helvetica-Bold'),
]))
story.append(dfd)
story.append(sp(10))

story += [
    sub('4.2  Process Flow'),
    body('<b>Member Booking Flow:</b>  Register → Login → Browse Packages → Select Package → '
         'Confirm Booking → View Booking Detail (with payment status) → Admin updates payment → Member sees updated status.'),
    sp(4),
    sub('4.3  Database Design'),
    body('The following tables are defined in the <i>gym</i> app models:'),
    sp(4),
    plain_table(
        [['Model / Table',    'Key Fields',                              'Relationships'],
         ['Category',         'id, name, description, created_at',       '—'],
         ['PackageType',      'id, name, description',                   '—'],
         ['Package',          'id, name, price, duration_months, is_active', 'FK → Category, PackageType'],
         ['Trainer',          'id, name, specialization, bio, experience_years', '—'],
         ['Equipment',        'id, name, description, quantity',         '—'],
         ['UserProfile',      'id, phone, address, date_of_birth',       'OneToOne → User'],
         ['Booking',          'id, start_date, end_date, total_amount, amount_paid, payment_status, booking_status', 'FK → User, Package'],
         ['ContactInquiry',   'id, name, email, phone, message, is_read','—'],],
        [TW*0.22, TW*0.42, TW*0.36],
    ),
    PageBreak(),
]

# ══════════════════════════════════════════════════════════════════
# PAGE 4 — SCREENSHOTS (described) + SOURCE CODE SNIPPETS
# ══════════════════════════════════════════════════════════════════
story += section('5. Screen Descriptions')
story += [
    body('The following key screens are available in the application:'),
    sp(4),
    plain_table(
        [['Screen',            'URL',                       'Access'],
         ['Homepage',          '/',                         'Public'],
         ['Packages List',     '/packages/',                'Public'],
         ['Package Detail',    '/packages/<id>/',           'Public'],
         ['Trainers',          '/trainers/',                'Public'],
         ['Equipment',         '/equipment/',               'Public'],
         ['Contact Us',        '/contact/',                 'Public'],
         ['Register',          '/accounts/register/',       'Public'],
         ['Login',             '/accounts/login/',          'Public'],
         ['Member Dashboard',  '/member/dashboard/',        'Login Required'],
         ['Profile Update',    '/accounts/profile/',        'Login Required'],
         ['Change Password',   '/accounts/change-password/','Login Required'],
         ['Booking Detail',    '/member/bookings/<id>/',    'Login Required'],
         ['Admin Panel',       '/admin/',                   'Admin Only'],],
        [TW*0.28, TW*0.38, TW*0.34],
    ),
    sp(10),
]

story += section('6. Source Code Highlights')
story += [
    sub('Booking Model (gym/models.py)'),
    Paragraph(
        'class Booking(models.Model):\n'
        '    user         = ForeignKey(User, on_delete=CASCADE)\n'
        '    package      = ForeignKey(Package, on_delete=CASCADE)\n'
        '    start_date   = DateField()\n'
        '    end_date     = DateField()\n'
        '    total_amount = DecimalField(max_digits=10, decimal_places=2)\n'
        '    amount_paid  = DecimalField(max_digits=10, decimal_places=2)\n'
        '    payment_status  = CharField(choices=[pending/partial/full])\n'
        '    booking_status  = CharField(choices=[active/expired/cancelled])\n\n'
        '    @property\n'
        '    def balance(self):  # auto-computed — not stored\n'
        '        return self.total_amount - self.amount_paid',
        Code),
    sp(6),
    sub('Book Package View (gym/views.py)'),
    Paragraph(
        '@login_required\n'
        'def book_package(request, pk):\n'
        '    package = get_object_or_404(Package, pk=pk, is_active=True)\n'
        '    if request.method == "POST":\n'
        '        start_date = date.today()\n'
        '        end_date   = start_date + timedelta(days=30 * package.duration_months)\n'
        '        Booking.objects.create(\n'
        '            user=request.user, package=package,\n'
        '            start_date=start_date, end_date=end_date,\n'
        '            total_amount=package.price, amount_paid=0,\n'
        '            payment_status="pending"\n'
        '        )\n'
        '        return redirect("booking_detail", pk=booking.pk)',
        Code),
    PageBreak(),
]

# ══════════════════════════════════════════════════════════════════
# PAGE 5 — USER GUIDE + DEVELOPER GUIDE
# ══════════════════════════════════════════════════════════════════
story += section('7. User Guide')
story += [
    sub('For Members'),
    bullet_list([
        '<b>Register:</b> Visit /accounts/register/, fill in your name, username, email, and password.',
        '<b>Login:</b> Use your username and password at /accounts/login/.',
        '<b>Browse Packages:</b> Go to /packages/ and filter by category. Click a package for full details.',
        '<b>Book a Package:</b> On any package detail page, click "Book This Package" and confirm.',
        '<b>View Bookings:</b> Your dashboard at /member/dashboard/ shows all bookings, payment status, and balance.',
        '<b>Update Profile:</b> Go to /accounts/profile/ to update your name, phone, address, and date of birth.',
        '<b>Change Password:</b> Use /accounts/change-password/ to set a new password securely.',
    ]),
    sp(6),
    sub('For Guests'),
    bullet_list([
        'Browse the homepage, packages list, trainers, and equipment pages without registering.',
        'Submit a contact inquiry via the Contact Us page — the gym will respond by phone or email.',
    ]),
    sp(8),
]

story += section('8. Developer\'s Guide')
story += [
    sub('8.1  Module Descriptions'),
    plain_table(
        [['App / Module',   'File',              'Purpose'],
         ['gym',            'models.py',         'Defines all database models: Category, Package, Booking, Trainer, Equipment, Contact'],
         ['gym',            'views.py',          'Handles all public-facing and member views — home, packages, booking, contact'],
         ['gym',            'admin.py',          'Registers all models with the Django admin with list filters, search, and editable fields'],
         ['gym',            'urls.py',           'URL routes for all gym pages including booking flow'],
         ['accounts',       'views.py',          'Handles registration, login, logout, profile update, password change, member dashboard'],
         ['accounts',       'forms.py',          'RegisterForm (UserCreationForm extension) and ProfileUpdateForm'],
         ['accounts',       'urls.py',           'URL routes for all account-related pages'],
         ['fitness_first',  'settings.py',       'Project settings — installed apps, templates dir, media/static paths, login redirects'],
         ['fitness_first',  'urls.py',           'Root URL config including admin, accounts, and gym URL includes'],
         ['templates/',     'base.html',         'Master layout: navbar, messages, footer, Bootstrap + custom CSS'],
         ['static/css/',    'style.css',         'Full custom stylesheet — feminine rose/pink palette, Poppins + Playfair Display fonts'],],
        [TW*0.18, TW*0.22, TW*0.60],
    ),
    sp(8),
    sub('8.2  Project Credits'),
    plain_table(
        [['Role',                        'Name',             'Contribution'],
         ['Developer',                   'Favor Chinonso',   'Full system design, coding, database modelling, UI/UX, testing and deployment'],
         ['Mentor & Project Supervisor', 'Jubril Bucknor',   'Project flow guidance, architecture review, technical oversight and quality assurance'],],
        [TW*0.30, TW*0.26, TW*0.44],
    ),
    sp(8),
    sub('8.3  Setup Instructions'),
    bullet_list([
        'Install Python 3.10+ and run:  pip3 install django reportlab',
        'Navigate to project folder and run:  python3 manage.py migrate',
        'Load sample data:  python3 manage.py shell &lt; seed_data.py',
        'Start server:  python3 manage.py runserver',
        'Access admin at http://127.0.0.1:8000/admin/  (admin / admin123)',
        'To add a new package: login to admin → Packages → Add Package.',
        'To update payment for a booking: admin → Bookings → select booking → update Amount Paid and Payment Status.',
    ]),
    sp(8),
    HRFlowable(width='100%', thickness=1, color=ROSE, spaceAfter=8),
    Paragraph('End of Report — Fitness First GYM Management System, Abuja, Nigeria, 2025', Small),
]

# ── Compile ───────────────────────────────────────────────────────────────────
doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
print("PDF generated: Fitness_First_Project_Report.pdf")
