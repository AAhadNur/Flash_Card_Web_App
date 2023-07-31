from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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


@login_required
def create_set(request):
    if request.method == "POST":
        form = CreateSetForm(request.POST)

        if form.is_valid():
            Set.objects.create(
                name=request.POST.get('name'),
                description=request.POST.get('description'),
                term_language=request.POST.get('term_language'),
                definition_language=request.POST.get('definition_language'),
                owner=request.user,
            )

            return redirect('home')

    else:
        form = CreateSetForm()

    context = {
        'form': form,
    }

    return render(request, 'cards/add_cards_and_sets.html', context)


@login_required
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


@login_required
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

    li = []
    size = len(cards)

    for card in cards:
        if card.box not in li:
            li.append(card.box)

    context = {
        'cards': cards,
        'page': page,
        'listi': li,
        'total_cards': size,
    }

    return render(request, 'cards/all_cards.html', context)


@login_required
def add_cards(request):
    page = 'add card'
    if request.method == "POST":
        form = AddCardForm(request.POST)

        if form.is_valid():
            card_set_id = request.POST.get('card_set')
            card_set = Set.objects.get(id=card_set_id)

            if card_set is not None:
                Card.objects.create(
                    question=request.POST.get('question'),
                    answer=request.POST.get('answer'),
                    card_set=card_set,
                    owner=request.user,
                )

                return redirect('add_card')

            else:
                messages.error(request, 'Your entered Set is wrong!!!')

    else:
        form = AddCardForm()

    context = {'form': form, 'page': page}

    return render(request, 'cards/add_cards_and_sets.html', context)


@login_required
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


@login_required
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


def all_box_view(request, box_num):
    page = 'all box cards'

    all_cards = Card.objects.all()
    cards = Card.objects.filter(box=box_num)

    li = []

    for card in all_cards:
        if card.box not in li:
            li.append(card.box)

    context = {
        'page': page,
        'cards': cards,
        'listi': li,
    }

    return render(request, 'cards/all_box_cards.html', context)
