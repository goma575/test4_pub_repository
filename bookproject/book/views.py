from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Avg
from django.core.paginator import Paginator

from .models import Book,Review
from .forms import ReviewForm

class ListBookView(ListView):
    template_name ="book/book_list.html"
    model = Book
    ordering="-id"
    # paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ranking_list = Book.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')
        paginator = Paginator(ranking_list, 5)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.page(page_number)
        context["ranking_list"]= page_obj
        return context   
    

class DetailBookView(LoginRequiredMixin,DetailView):
    template_name ="book/book_detail.html"
    model = Book

class CreateBookView(LoginRequiredMixin,CreateView):
    template_name ="book/book_create.html"
    model = Book
    fields=('title','text','category','thumbnail')
    success_url=reverse_lazy("list-book")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class DeleteBookView(LoginRequiredMixin,DeleteView):
    template_name ="book/book_confirm_delete.html"
    model = Book
    success_url=reverse_lazy("list-book")
    def get_object(self,queryset=None):
        obj=super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj


class UpdateBookView(LoginRequiredMixin,UpdateView):
    template_name ="book/book_update.html"
    model = Book
    fields="__all__"
    success_url=reverse_lazy("list-book")
    def get_object(self,queryset=None):
        obj=super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj
    

class CreateReviewView(LoginRequiredMixin,CreateView):
    template_name="book/review_form.html"
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hoge"]="hogehoge"
        print(self.request.user,"WWWWWWWWWWWWW")
        context["book"]=Book.objects.get(id =self.kwargs["book_id"])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        book = Book.objects.get(id=self.kwargs["book_id"]) 
        form.instance.book = book 
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("detail-book",kwargs={"pk":self.object.book_id})












#関数ベースでDBからレコードを取り出す
def index(request):
    #空のディクショナリ作成
    context = {}
    #object_listキーを指定,レコード取り出し
    context["object_list"]=Book.objects.all()  #objectsメソッドでレコードに対する操作を指定。all()はすべて取り出す
    context["hoge"]="hogehoge"
    print(context["object_list"])
    #book/book.htmlにcontext(辞書)を渡す
    return render(request,"book/book_list.html",context)



#保存処理関数ベースビュー版。これはポスト専用(getの時の処理は書いてません。)。getの方法はまた今度。
# def create(request):
#     #ターミナルにpostされたデータが表示されるよ。
#     print(request.POST)
#     #空のインスタンス作って、属性（テーブルのカラムにデータを入れてく。）
#     new_reco=Book()
#     #new_reco.title=request.POST["title"] #ほんとにこれでいいの？
#     new_reco.title=request.POST.get("title","タイトルがなかった時の処理") #こっちの方がまだベター。
#     new_reco.text=request.POST["text"]
#     new_reco.category=request.POST["category"]
#     #属性を入れたインスタンスを保存する。
#     new_reco.save()
#     #トップに移動する。
#     return redirect("book-list")
    