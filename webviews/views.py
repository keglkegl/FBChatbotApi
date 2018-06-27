from django.shortcuts import render


def nlb_faq_list(request):
    return render(request, 'NLB_faq/nlb_faq_list.html')