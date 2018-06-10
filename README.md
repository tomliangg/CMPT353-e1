# CMPT353-e1
<h3>This repo is created for documentation purpose. The repo contains my personal work toward the SFU CMPT353 (Computational Data Science) course. You may use my solution as a reference. The .zip archive contains the original exercise files. For practice purpose, you can download the .zip archive and start working from there.</h3>

<p><a href="https://coursys.sfu.ca/2018su-cmpt-353-d1/pages/AcademicHonesty">Academic Honesty</a>: it's important, as always.</p>
<p>Below is the exercise description </p>
<hr>

<div class="wikicontents creole tex2jax_ignore"><p>Due <span title="2018-05-18T23:59:59-07:00">Friday May 18 2018</span>.</p>
<p>This exercise is designed to help you get used to the NumPy and Pandas APIs. To force you to do this, <strong>you may not write any loops</strong> in your code: no <code>for</code>, no <code>while</code>, no list comprehensions, no recursion. All iteration can be handled by calls to relevant functions in the libraries that will iterate for you.</p>
<p>Some files are provided that you need below: <a href="E1.zip">E1.zip</a>.</p>
<h2 id="h-python-libraries">Python Libraries</h2>
<p>Before you get started, you will need some Python libraries installed. See the <a href="InstallingPython">InstallingPython</a> page for some ways to do that and instructions. </p>
<p>For this week, you'll need at least the <code>numpy</code>, <code>pandas</code>, <code>statsmodels</code>, and <code>jupyter</code> libraries. You can install the others mentioned there if you like: they will be used later in the course.</p>
<h2 id="h-getting-started-with-jupyter">Getting Started with Jupyter</h2>
<p>Let's start with a Jupyter Notebook (which you may have previsouly heard of called an iPython Notebook: it has been renamed). If you have the Jupyter package installed, you can run the command <span>&ldquo;</span><code>jupyter notebook</code><span>&rdquo;</span> or if you installed Anaconda, run its <span>&ldquo;</span>Jupyter Notebook<span>&rdquo;</span>. See my <a href="Jupyter">Jupyter instructions</a> for more information on getting started.</p>
<p>Experiment a little to see how it works. In particular, pressing enter starts a new line of code and control-enter runs the cell where your cursor is.</p>
<p>The first task will be to do a simple data processing kind of task: create arrays holding data for a sine wave <span>&ldquo;</span>signal<span>&rdquo;</span>; simulate a noisy sensor reading that signal; plot both; use a signal processing filter to try to reconstruct the true signal fromt he noisy data.</p>
<p>Have a look at a <a href="E1-jupyter/view">screenshot of my notebook</a>, which does this, but has a few parts redacted so you don't get bored. Plot formatting varies a little between versions (or browsers or operating systems or something): if they look slightly different, that's okay.</p>
<p><strong>Create a Jupyter notebook</strong> that reproduces my calculations, named <code>signal-plot.ipynb</code>.</p>
<h2 id="h-getting-started-with-numpy">Getting Started with NumPy</h2>
<p>Download the NumPy data archive <code>monthdata.npz</code>. This has two arrays containing information about precipitation in Canadian cities (each row represents a city) by month (each column is a month Jan<span>&ndash;</span>Dec of a particular year). The arrays are the total precipitation observed on different days, and the number of observations recorded. You can get the NumPy arrays out of the data file like this:</p>
<pre class="highlight lang-python">data = np.load('monthdata.npz')
totals = data['totals']
counts = data['counts']</pre>
<p>Use this data to find these things:</p>
<ul><li>Which city had the lowest total precipitation over the year? Hints: sum across the rows (axis 1); use <code>argmin</code> to determine which row has the lowest value. Print the row number.
</li><li>Determine the average precipitation in these locations for each month. That will be the total precipitation for each month (axis 0), divided by the total observations for that months. Print the resulting array.
</li><li>Do the same for the cities: give the average daily precipitation for each city by printing the array.
</li><li>Calculate the total precipitation for each quarter in each city (i.e. the totals for each station across three-month groups). You can assume the number of columns will be divisible by 3. Hint: use the <a href="https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html">reshape function</a> to reshape to a 4<em>n</em> by 3 array, sum, and reshape back to <em>n</em> by 4.
</li></ul>
<p><strong>Write a Python program <code>np_summary.py</code></strong> that produces the values specified here. Its output should exactly match the provided <code>np_summary.txt</code>. We will test it on a different set of inputs: your code <strong>should not assume</strong> there is a specific number of weather stations. You can assume that there is exactly one year (12 months) of data.</p>
<h2 id="h-getting-started-with-pandas">Getting Started with Pandas</h2>
<p>To get started with Pandas, we will repeat the analysis we did with Numpy. Pandas is more data-focussed and is more friendly with its input formats. We can use nicely-formatted CSV files, and read it into a Pandas dataframe like this:</p>
<pre class="highlight lang-python">totals = pd.read_csv('totals.csv').set_index(keys=['name'])</pre>
<p>This is the same data, but has the cities and months labelled, which is nicer to look at.</p>
<p>Reproduce the values you calculated with NumPy, <strong>except</strong> the quarterly totals, which are a bit of a pain. The difference will be that you can produce more informative output, since the actual months and cities are known. When you print a Pandas DataFrame or series, the format will be nicer.</p>
<p><strong>Write a Python program <code>pd_summary.py</code></strong> that produces the values specified here. Its output should exactly match the provided <code>pd_summary.txt</code>.</p>
<h2 id="h-analysis-with-pandas">Analysis with Pandas</h2>
<p>The data in the provided files had to come from <em>somewhere</em>. What you got started with 180MB of data for 2016 from the <a href="https://www.ncdc.noaa.gov/data-access/land-based-station-data/land-based-datasets/global-historical-climatology-network-ghcn">Global Historical Climatology Network</a>. To get the data down to a reasonable size, filtered out all but a few weather stations and precipitation values, joined in the names of those stations, and got the file provided as <code>precipitation.csv</code>.</p>
<p>The data in <code>precipitation.csv</code> is a fairly typical result of joining tables in a database, but not easy to analyse as you did above.</p>
<p><strong>Create a program <code>monthly_totals.py</code></strong> that recreates the <code>totals.csv</code>, <code>counts.csv</code>, and <code>monthdata.npz</code> files as you originally got them. The provided <code>monthly_totals_hint.py</code> provides an outline of what needs to happen. You need to fill in the <code>pivot_months_pandas</code> function (and leave the other parts intact for the next part).</p>
<ol><li>Add a column 'month' that contains the results of applying the <code>date_to_month</code> function to the existing 'date' column. [You may have to modify <code>date_to_month</code> slightly, depending how your data types work out. ]
</li><li>Use the Pandas <a href="http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html">groupby method</a> to aggregate over the name and month columns. Sum each of the aggregated values to get the total. Hint: <code>grouped_data.aggregate('sum').reset_index()</code>
</li><li>Use the Pandas <a href="http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.pivot.html">pivot method</a> to create a row for each station (name) and column for each month.
</li><li>Repeat with the 'count' aggregation to get the count of observations.
</li></ol>
<p>When you submit, make sure your code is using the <code>pivot_months_pandas</code> function you wrote.</p>
<h2 id="h-timing-comparison">Timing Comparison</h2>
<p>Use the provided <code>timing.ipynb</code> notebook to test your function against the <code>pivot_months_loops</code> function that I wrote. (It should import into the notebook as long as you left the <code>main</code> function and <code>__name__ == '__main__'</code> part intact.)</p>
<p>The notebook runs the two functions and ensures that they give the same results. It also uses <a href="https://ipython.org/ipython-doc/3/interactive/magics.html#magic-timeit">the %timeit magic</a> (which uses <a href="https://docs.python.org/3/library/timeit.html">Python timeit</a>) to do a simple benchmark of the functions.</p>
<p>Run the notebook. Make sure all is well, and compare the running times of the two implementations.</p>
<h2 id="h-questions">Questions</h2>
<p>Answer these questions in a file <code>answers.txt</code>. [Generally, these questions should be answered in a few sentences each.]</p>
<ol><li>Where you did the same calculations with NumPy and Pandas, which did you find easier to work with? Which code do you think is easier to read?
</li><li>What were the running times of the two <code>pivot_months_*</code> functions? How can you explain the difference?
</li></ol>
<h2 id="h-submitting">Submitting</h2>
<p>Submit your files through CourSys for <a href="/2018su-cmpt-353-d1/+e1/">Exercise 1</a>.</p></div>

<div class="updateinfo">Updated Wed April 04 2018, 09:20 by ggbaker.

</div>
