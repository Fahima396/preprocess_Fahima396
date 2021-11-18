from preprocess_Fahima396 import utils

__version__ = '0.0.1'

def get_wordcounts(x):
	return utils.get_wordcounts(x)

def get_charcounts(x):
	return utils.get_charcounts(x)

def get_avg_wordlength(x):
	return utils.get_avg_wordlength(x)

def get_stopwords_counts(x):
	return utils.get_stopwords_counts(x)

def get_hashtag_counts(x):
	return utils.get_hashtag_counts(x)

def get_mentions_counts(x):
	return utils.get_mentions_counts(x)

def get_digit_Counts(x):
	return utils.get_digit_Counts(x)

def get_uppercase_counts(x):
	return utils.get_uppercase_counts(x)

def get_cont_exp(x):
	return utils.get_cont_exp(x)

def get_emails(x):
	return utils.get_emails(x)

def remove_emails(x):
	return utils.remove_emails(x)

def get_urls(x):
	return utils.get_urls(x)

def remove_urls(x):
	return utils.remove_urls(x)

def remove_rt(x):
	return utils.remove_rt(x)

def remove_special_chars(x):
	return utils.remove_special_chars(x)

def remove_html_tags(x):
	return utils.remove_html_tags(x)

def remove_accented_chars(x):
	return utils.remove_accented_chars(x)

def remove_stopwords(x):
	return utils.remove_stopwords(x)

def make_base(x):
	return utils.make_base(x)

def remove_common_words(x, n=20):
	return utils.remove_common_words(x, n=20)

def remove_rarewords(x, n=20):
	return utils.remove_rarewords(x, n=20)

def spelling_correction(x):
	return utils.spelling_correction(x)