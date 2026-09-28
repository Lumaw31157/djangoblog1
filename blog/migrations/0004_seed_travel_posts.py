from django.db import migrations


CATEGORIES = ["Destinations", "Tips", "Food"]

POSTS = [
    {
        "title": "Sunrise Over a Thousand Temples in Bagan",
        "category": "Destinations",
        "content": (
            "Waking up before dawn in Bagan is worth every yawn. Hundreds of "
            "ancient temples rise out of the morning mist as hot air balloons "
            "drift overhead. Rent an e-bike, pick a quiet pagoda away from the "
            "crowds, and watch the sky turn gold. Bring a scarf for the dusty roads "
            "and plenty of water for the midday heat."
        ),
    },
    {
        "title": "A Slow Weekend on Inle Lake",
        "category": "Destinations",
        "content": (
            "Life on Inle Lake moves at the pace of a paddle. Stilted villages, "
            "floating gardens, and fishermen rowing with one leg make this one of "
            "the most peaceful places to spend a weekend. Stay in a lakeside "
            "guesthouse, take a slow boat tour in the early morning, and visit a "
            "local weaving workshop before the tourist boats arrive."
        ),
    },
    {
        "title": "Chasing Waterfalls in Ha Giang",
        "category": "Destinations",
        "content": (
            "The mountain roads of Ha Giang wind past terraced rice fields and "
            "hidden waterfalls that rarely make it into guidebooks. A motorbike "
            "loop over a few days is the best way to see it, but check your brakes "
            "before the descents and carry cash, since ATMs are scarce once you "
            "leave the main town."
        ),
    },
    {
        "title": "Best Time to Visit Japan for Fewer Crowds",
        "category": "Destinations",
        "content": (
            "Cherry blossom season gets all the attention, but late autumn offers "
            "the same postcard scenery with a fraction of the crowds. Aim for "
            "early November for crisp air and red maple leaves, and consider "
            "smaller cities like Kanazawa or Takayama instead of Tokyo and Kyoto "
            "alone."
        ),
    },
    {
        "title": "The Hidden Beaches of the Andaman Coast",
        "category": "Destinations",
        "content": (
            "Past the resorts and day-trip boats, a handful of beaches on the "
            "Andaman coast stay quiet even in high season. Ask local longtail "
            "boat drivers rather than tour desks, and plan to spend a full day "
            "so you're not rushed off before sunset."
        ),
    },
    {
        "title": "Packing Light for Long Trips",
        "category": "Tips",
        "content": (
            "A carry-on bag and a packing cube system can carry you through a "
            "month of travel. Stick to a simple color palette so everything "
            "mixes and matches, pack one layer for warmth, and leave room for "
            "the things you'll inevitably pick up along the way."
        ),
    },
    {
        "title": "Budget Travel Tips for Southeast Asia",
        "category": "Tips",
        "content": (
            "Southeast Asia rewards travelers who slow down. Take overnight "
            "buses to save on a night's accommodation, eat where the locals eat, "
            "and book guesthouses a day or two in advance instead of weeks ahead "
            "to catch better rates."
        ),
    },
    {
        "title": "How to Plan a Road Trip Itinerary",
        "category": "Tips",
        "content": (
            "The best road trips leave room to change plans. Pick two or three "
            "must-see anchor points, keep driving days under five hours, and "
            "leave at least one day completely unplanned for the places you "
            "discover along the way."
        ),
    },
    {
        "title": "Solo Travel: What I Learned",
        "category": "Tips",
        "content": (
            "Traveling alone forces you to talk to strangers, trust your own "
            "judgment, and slow down enough to actually notice a place. Share "
            "your rough plans with someone back home, stay in social "
            "guesthouses if you want company, and don't be afraid to eat at a "
            "restaurant by yourself."
        ),
    },
    {
        "title": "Street Food You Must Try in Bangkok",
        "category": "Food",
        "content": (
            "Bangkok's street stalls often outshine its restaurants. Look for "
            "the carts with the longest local queues, try pad kra pao from a "
            "wok-fired stall, and save room for mango sticky rice from a vendor "
            "near Chinatown."
        ),
    },
]


def seed_data(apps, schema_editor):
    Category = apps.get_model('blog', 'Category')
    Post = apps.get_model('blog', 'Post')
    from django.utils.text import slugify

    category_objs = {}
    for name in CATEGORIES:
        cat, _ = Category.objects.get_or_create(name=name, defaults={'slug': slugify(name)})
        category_objs[name] = cat

    for item in POSTS:
        slug = slugify(item["title"])
        if not Post.objects.filter(slug=slug).exists():
            Post.objects.create(
                title=item["title"],
                slug=slug,
                content=item["content"],
                excerpt=item["content"][:150],
                category=category_objs[item["category"]],
                status='published',
            )


def remove_data(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Category = apps.get_model('blog', 'Category')
    titles = [item["title"] for item in POSTS]
    Post.objects.filter(title__in=titles).delete()
    Category.objects.filter(name__in=CATEGORIES).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_post_excerpt_post_category'),
    ]

    operations = [
        migrations.RunPython(seed_data, remove_data),
    ]
