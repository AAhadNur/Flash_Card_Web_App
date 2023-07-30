from django.shortcuts import render, redirect, get_object_or_404

from cards.models import Card, Set
from cards.forms import AddCardForm, CreateSetForm

# Create your views here.


def homepage(request):
    card_sets = Set.objects.all()

    context = {
        'card_sets': card_sets,
    }

    return render(request, 'cards/all_cards_and_sets.html', context)


def individual_set(request, pk):
    page = 'all set cards'
    card_set = Set.objects.get(id=pk)

    cards = card_set.card_set.all()

    li = []

    for card in cards:
        if card.box not in li:
            li.append(card.box)

    context = {
        'cards': cards,
        'page': page,
        'listi': li,
    }
    return render(request, 'cards/all_cards_and_sets.html', context)


def create_set(request):
    if request.method == "POST":
        form = CreateSetForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')

    else:
        form = CreateSetForm()

    context = {
        'form': form,
    }

    return render(request, 'cards/add_cards_and_sets.html', context)


def update_set(request, pk):
    card_set = Set.objects.get(id=pk)

    if request.method == "POST":
        form = CreateSetForm(request.POST, instance=card_set)

        if form.is_valid():
            form.save()

            return redirect('all_sets')

    else:
        form = CreateSetForm(instance=card_set)

    context = {
        'form': form,
    }

    return render(request, 'cards/update_card_and_set.html', context)


def delete_set(request, pk):
    page = 'set'
    card_set = Set.objects.get(id=pk)

    if request.method == 'POST':
        card_set.delete()
        return redirect('home')

    context = {
        'obj': card_set,
        'page': page,
    }
    return render(request, 'cards/delete.html', context)


def all_cards(request):
    page = 'all cards'
    cards = Card.objects.all()

    context = {
        'cards': cards,
        'page': page,
    }

    return render(request, 'cards/all_cards_and_sets.html', context)


def add_cards(request):
    page = 'add card'
    if request.method == "POST":
        form = AddCardForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('add_card')

    else:
        form = AddCardForm()

    context = {'form': form, 'page': page}

    return render(request, 'cards/add_cards_and_sets.html', context)


def edit_card(request, pk):
    page = 'edit card'
    card = Card.objects.get(id=pk)

    if request.method == "POST":
        form = AddCardForm(request.POST, instance=card)

        if form.is_valid():
            form.save()

            return redirect('all_cards')

    else:
        form = AddCardForm(instance=card)

    context = {'form': form, 'page': page}

    return render(request, 'cards/update_card_and_set.html', context)


def delete_card(request, pk):
    card = Card.objects.get(id=pk)

    card_set = card.card_set

    if request.method == 'POST':
        card.delete()
        if card_set is not None:
            return redirect('set_cards', pk=card_set.id)
        else:
            return redirect('all_cards')

    context = {
        'obj': card,
    }
    return render(request, 'cards/delete.html', context)


def box_view(request, pk, box_num):
    page = 'all box cards'
    card_set = Set.objects.get(id=pk)
    all_cards = card_set.card_set.all()
    cards = card_set.card_set.filter(box=box_num)

    li = []

    for card in all_cards:
        if card.box not in li:
            li.append(card.box)

    context = {
        'page': page,
        'cards': cards,
        'listi': li,
    }

    return render(request, 'cards/all_cards_and_sets.html', context)
