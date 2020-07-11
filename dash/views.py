from django.shortcuts import render
from accounts.models import Profile
from shop.models import Purchase, Product

# Create your views here.


def dash(request):
    purchases = Purchase.objects.all().order_by('-created')
    consumers = Profile.objects.all()
    total_consumers = consumers.count()
    total_purchases = purchases.count()
    delivered_purchases = purchases.filter(status='D').count()
    purchases_in_progress = purchases.filter(status='I').count()

    filtered_consumers = Profile.objects.all().order_by('-created')
    filtered_purchases = []
    consumers_and_their_purchases = {}
    count = 0
    for user in filtered_consumers:
        related_purchases = Purchase.objects.filter(consumer=user.pk)
        total_related_purchases = related_purchases.count()
        filtered_purchases.append(total_related_purchases)
        consumers_and_their_purchases[user] = filtered_purchases[count]
        count += 1

    context = {
        'consumers_and_purchases': consumers_and_their_purchases,
        'purchases': purchases,
        'total_consumers': total_consumers,
        'total_purchases': total_purchases,
        'delivered_purchases': delivered_purchases,
        'purchases_in_progress': purchases_in_progress
    }

    return render(request, 'dashboard.html', context)
