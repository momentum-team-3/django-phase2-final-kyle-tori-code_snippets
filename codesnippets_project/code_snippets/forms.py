from django.forms import Form, ChoiceField, CharField

class SearchForm(Form):
    SEARCH_BY = (('includes', 'includes'), ('starts with', 'starts with'), ('exact match', 'exact match'))
    title = CharField(label='Snippet title')
    title_search_by = ChoiceField(label='Search title by', choices=SEARCH_BY, initial='includes')
    text = CharField(label='Snippet text')
    text_search_by = ChoiceField(label='Search text by', choices=SEARCH_BY, initial='includes')
    language = CharField(label='Snippet Language')
    language_search_by = ChoiceField(label='Search language for', choices=SEARCH_BY, initial='includes')

