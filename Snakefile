length = list(range(1, 16))


rule all:
    input:
        expand("results/filtered_data/length_{length}.tsv", length=length)


rule count_parts:
    input:
        "resources/data.fa"
    output:
        "results/count_parts/length_{length}.tsv"
    script:
        "workflow/scripts/count_parts.py"

rule analyze_frequnzy:
    input:
        "results/count_parts/length_{length}.tsv"
    output:
        "results/analyze_frequenzy/frequnzy_length_{length}.tsv"
    script:
        "workflow/scripts/analyze_frequency.py"

rule create_plots:
    input:
        "results/analyze_frequenzy/frequnzy_length_{length}.tsv"
    output:
        "results/make_plots/length_{length}.png"
    script:
        "workflow/scripts/make_plots.py"


rule calculate_mean_and_std:
    input:
        "results/analyze_frequenzy/frequnzy_length_{length}.tsv"
    output:
        "results/mean_and_std/mean_and_std_{length}.csv"
    script:
        "workflow/scripts/calculate_mean_and_std.py"


rule filter_data:
    input:
        "results/count_parts/length_{length}.tsv",
        "results/mean_and_std/mean_and_std_{length}.csv"
    output:
        "results/filtered_data/length_{length}.tsv"
    script:
        "workflow/scripts/filter_data.py"

# Please run find clusters.py and sort_clusters.py






