from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_financial_data(request):
    data = [
        {
            "label": "Income",
            "backgroundColor": "#4F46E5",
            "data": [3000, 4500, 7500, 9500, 12000, 14000],
        },
        {
            "label": "Expenses",
            "backgroundColor": "#F87171",
            "data": [2000, 3500, 5000, 8000, 11000, 12000],
        },
    ]
    return Response(data)

@api_view(['GET'])
def get_balance(request):
    data = {"name": "balance", "amount": 5000}
    return Response(data)


@api_view(['GET'])
def recent_activities_data(request):
    data = [
        {
            "label": "Netflix Subscription",
            "link": "data:image/png;base64,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",
            "amount": 2200,
            "type": "debite"
        },
        {
            "label": "Amazon Subscription",
            "link": "data:image/png;base64,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",
            "amount": 4200,
            "type": "debite"
        },
        {
            "label": "Canva Subscription",
            "link": "https://images-eds-ssl.xboxlive.com/image?url=4rt9.lXDC4H_93laV1_eHHFT949fUipzkiFOBH3fAiZZUCdYojwUyX2aTonS1aIwMrx6NUIsHfUHSLzjGJFxxo4K81Ei7WzcnqEk8W.MgwadpHjl76SlQnWKc4OkaILTy7aDmpraBC2vB.Q_eb6EavJPyLEBEEqc.BSkZzu5Vng-&format=source",
            "amount": 3200,
            "type": "debite"
        },
    ]
    return Response(data)


@api_view(['GET'])
def get_savings_plans(request):
    savings_plans = [
        {"name": "New Car", "amount": 20000},
        {"name": "New House", "amount": 32000},
        {"name": "Vacation", "amount": 45000},
    ]
    return Response(savings_plans)
