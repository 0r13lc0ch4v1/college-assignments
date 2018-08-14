


<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta name="author" content="Floobits" />
  <meta name="viewport" content="width=1000" />
  <link rel="shortcut icon" href="/favicon.ico" />
  
  <script type="text/javascript" src="/static/js/extern/jquery-2.2.0.min.js" crossorigin="anonymous"></script>
  <script type="text/javascript" src="/static/js/extern/bootstrap-3.3.6.min.js" crossorigin="anonymous"></script>
  
  

  <title>Floobits</title>
  <link rel="stylesheet" href="/static/CACHE/css/8feb4bd8cf12.css" type="text/css" media="all" />
  <script type="text/javascript">
if (typeof console === "undefined") {
  this.console = {
    error: function () {},
    log: function () {},
    warn: function () {}
  };
}

if (!console.error) {
  console.error = console.log;
}
if (!console.warn) {
  console.warn = console.log;
}

console.log("Why hello there. Your prize for opening the developer console is this information: We hang out in #floobits on Freenode.");
</script>

  <script type="text/javascript">
  var global = this;
  global.fl = {
    "csrfToken": "AY7OQIDG8W8OnKTRmiKYndmxJdMX7PN9v1kYkbp793yQ41wWVi9LKmZdG2bdnRKE"
  };
  _eventTracker = [];
</script>

  


  
  
</head>
<body >
  
    
    
    <div id="watch-us-code" class="watch-us-code" style="display:none;">
      <div class="wrap">
        <a id="watch-us-code-href" href="//">Watch us code!</a>
      </div>
    </div>
  
  <main>
    
      <nav class="navbar navbar-default fl-navbar " role="navigation">
  <div class="container">
    <div class="container-fluid">
      <div class="navbar-header">
        <a href="/">
          <img src="/static/images/v2/fl_logo146_30.png" width="146" height="30" alt="Floobits" title="Floobits" />
        </a>
        
      </div>
      <ul class="nav navbar-nav navbar-right navbar-authed">
  
    <li class="fl-nav-user-image">
      <a style="display: inline; padding: 0; margin: 0;" href="/dash">
        <img class="gravatar" src="https://secure.gravatar.com/avatar/b8ca07714e88b03ad8cf6f41cd5c7165?d=retro&s=100" alt="Oriel's Gravatar" />
      </a>
    </li>
    <li class="fl-nav-user"><a class="fl-nav-link" href="/dash">
      Oriel</a></li>
    
    <li><a class="fl-nav-link" href="/Oriel/settings">settings</a></li>
    <li><a class="fl-nav-link" href="/logout">logout</a></li>
  
  <li><a class="fl-nav-link" href="/help">help</a></li>
  <li><a class="fl-nav-link" href="https://news.floobits.com/">news</a></li>
</ul>
    </div>
  </div>
</nav>

    
    
  <div class="tab-container">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <h1 class="content-title">
  <a href="/Oriel">
    <img style="width: 50px; height: 50px; border-radius: 25px; margin-top: -10px;" src="https://secure.gravatar.com/avatar/b8ca07714e88b03ad8cf6f41cd5c7165?d=retro&amp;s=100"/> Oriel</a>
  /
  <a class="info-workspace-name" href="/Oriel/simulation/info">simulation</a>
</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <ul class="nav nav-tabs">
            
  <li >
    <a href="/Oriel/simulation/info">
      <i class="glyphicon glyphicon-info-sign"></i>
      Info
    </a>
  </li>
  <li >
    <a href="/Oriel/simulation">
      <i class="glyphicon glyphicon-edit"></i>
      Web Editor
    </a>
  </li>
  <li >
    <a href="/Oriel/simulation/browse">
      <i class="glyphicon glyphicon-folder-close"></i>
      Browse Code
    </a>
  </li>
  
    <li >
      <a href="/Oriel/simulation/settings">
        <i class="glyphicon glyphicon-cog"></i>
        Settings
      </a>
    </li>
    <li >
      <a href="/Oriel/simulation/permissions">
        <i class="glyphicon glyphicon-flag"></i>
        Permissions
      </a>
    </li>
  

          </ul>
        </div>
      </div>
    </div>
  </div>
  
  <div class="content-container">
    <div class="container">
      
        
      

      
<h3>
  
    <a href="/Oriel/simulation/browse">
  
  <i class="glyphicon glyphicon-file"></i>
  &nbsp;Oriel/simulation/</a>main_handler.py
  
    <a class="pull-right" href="/Oriel/simulation/raw/main_handler.py">
      <button type="button" class="btn btn-primary">Raw file</button>
    </a>
  
</h3>


  
    
      <style type="text/css">
        .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
      </style>
    
    <table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77</pre></div></td><td class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="kn">as</span> <span class="nn">plt</span>
<span class="kn">from</span> <span class="nn">roads_handler</span> <span class="kn">import</span> <span class="n">RoadsHandler</span>

<span class="k">def</span> <span class="nf">analyse_data</span><span class="p">(</span><span class="n">roadsHandler</span><span class="p">):</span>
    <span class="n">roads_pvj</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">bridge_pvj</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">roadsHandler</span><span class="o">.</span><span class="n">roads</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">k</span> <span class="o">!=</span> <span class="nb">len</span><span class="p">(</span><span class="n">roadsHandler</span><span class="o">.</span><span class="n">roads</span><span class="p">):</span>
            <span class="n">_round</span> <span class="o">=</span> <span class="n">roadsHandler</span><span class="o">.</span><span class="n">roads</span><span class="p">[</span><span class="n">k</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">_round</span> <span class="o">=</span> <span class="n">roadsHandler</span><span class="o">.</span><span class="n">bridge</span>

        <span class="n">p</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">v</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">j</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">avg_p</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">avg_v</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">avg_j</span> <span class="o">=</span> <span class="mi">0</span>

        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">_round</span><span class="o">.</span><span class="n">num_of_cars</span><span class="p">)):</span>
            <span class="n">p_temp</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="n">_round</span><span class="o">.</span><span class="n">num_of_cars</span><span class="p">[</span><span class="n">i</span><span class="p">])</span> <span class="o">/</span> <span class="n">_round</span><span class="o">.</span><span class="n">road_size</span>
            <span class="n">p</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">p_temp</span><span class="p">)</span>
            <span class="n">v_temp</span> <span class="o">=</span> <span class="mi">0</span>
            <span class="k">if</span> <span class="n">_round</span><span class="o">.</span><span class="n">num_of_cars</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">v_temp</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="n">_round</span><span class="o">.</span><span class="n">num_of_moved_cars</span><span class="p">[</span><span class="n">i</span><span class="p">])</span> <span class="o">/</span> <span class="n">_round</span><span class="o">.</span><span class="n">num_of_cars</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
                <span class="n">v</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">v_temp</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">v</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
            <span class="n">j_temp</span> <span class="o">=</span> <span class="n">p_temp</span> <span class="o">*</span> <span class="n">v_temp</span>
            <span class="n">j</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">j_temp</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">tik</span> <span class="ow">in</span> <span class="n">p</span><span class="p">:</span>
            <span class="n">avg_p</span> <span class="o">+=</span> <span class="n">tik</span>
        <span class="n">avg_p</span> <span class="o">/=</span> <span class="nb">len</span><span class="p">(</span><span class="n">_round</span><span class="o">.</span><span class="n">num_of_cars</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">tik</span> <span class="ow">in</span> <span class="n">v</span><span class="p">:</span>
            <span class="n">avg_v</span> <span class="o">+=</span> <span class="n">tik</span>
        <span class="n">avg_v</span> <span class="o">/=</span> <span class="nb">len</span><span class="p">(</span><span class="n">_round</span><span class="o">.</span><span class="n">num_of_cars</span><span class="p">)</span>

        <span class="n">avg_j</span> <span class="o">=</span> <span class="n">avg_p</span> <span class="o">*</span> <span class="n">avg_v</span>

        <span class="c1"># plt.plot(range(len(p)), p)</span>
        <span class="n">s</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">p</span><span class="p">)):</span>
            <span class="n">s</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="o">/</span> <span class="nb">float</span><span class="p">((</span><span class="nb">len</span><span class="p">(</span><span class="n">p</span><span class="p">))))</span>

        <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">p</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">,</span> <span class="n">s</span><span class="p">,</span> <span class="n">v</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="n">s</span><span class="p">,</span> <span class="n">j</span><span class="p">,</span> <span class="s1">&#39;g&#39;</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">k</span> <span class="o">!=</span> <span class="nb">len</span><span class="p">(</span><span class="n">roadsHandler</span><span class="o">.</span><span class="n">roads</span><span class="p">):</span>
            <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Road &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">k</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
            <span class="n">roads_pvj</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">p</span><span class="p">,</span> <span class="n">v</span><span class="p">,</span> <span class="n">j</span><span class="p">])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Bridge&quot;</span><span class="p">)</span>
            <span class="n">bridge_pvj</span> <span class="o">=</span> <span class="p">[</span><span class="n">p</span><span class="p">,</span> <span class="n">v</span><span class="p">,</span> <span class="n">j</span><span class="p">]</span>

        <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

    <span class="n">s</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">p</span><span class="p">)):</span>
        <span class="n">s</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="o">/</span> <span class="nb">float</span><span class="p">((</span><span class="nb">len</span><span class="p">(</span><span class="n">p</span><span class="p">))))</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">roads_pvj</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">2</span><span class="p">],</span> <span class="s1">&#39;r&#39;</span><span class="p">,</span> <span class="n">s</span><span class="p">,</span> <span class="n">bridge_pvj</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="n">s</span><span class="p">,</span> <span class="n">roads_pvj</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="mi">2</span><span class="p">],</span> <span class="s1">&#39;g&#39;</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;flow in Road1, Bridge, Road 4&quot;</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

    <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">roads_pvj</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">],</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Road 1 Velocity&quot;</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

    <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">roads_pvj</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Road 1 Density&quot;</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">run_simulation</span><span class="p">(</span><span class="n">num_of_roads</span><span class="p">,</span> <span class="n">size_of_road</span><span class="p">,</span> <span class="n">size_of_bridge</span><span class="p">,</span> <span class="n">T</span><span class="p">,</span> <span class="n">t0</span><span class="p">):</span>
    <span class="n">roadsHandler</span> <span class="o">=</span> <span class="n">RoadsHandler</span><span class="p">(</span><span class="n">num_of_roads</span><span class="p">,</span> <span class="n">size_of_road</span><span class="p">,</span> <span class="n">size_of_bridge</span><span class="p">)</span>
    <span class="n">roadsHandler</span><span class="o">.</span><span class="n">manage_simulation</span><span class="p">(</span><span class="n">T</span><span class="p">,</span> <span class="n">t0</span><span class="p">)</span>
    <span class="n">analyse_data</span><span class="p">(</span><span class="n">roadsHandler</span><span class="p">)</span>
</pre></div>
</td></tr></table>
  


    </div>
  </div>
  

    
      
<div class="fl-footer">
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <h5>Info</h5>
        <ul>
          
          <li><a href="/plans">Plans</a></li>
          
          <li><a href="/about">About Us</a></li>
          <li><a href="/pledge">Pledge</a></li>
          <li><a href="/security">Security</a></li>
          <li><a href="/edu">Education</a></li>
          <li><a href="/enterprise">Enterprise</a></li>
          <li><a href="/privacy">Privacy Policy</a></li>
          <li><a href="/tos">Terms of Service</a></li>
          <li><a href="/credits">Credits</a></li>
          <li><a href="/logos">Logos</a></li>
        </ul>
      </div>

      <div class="col-md-3">
        <h5>Help</h5>
        <ul>
          <li><a href="/help/faq">FAQ</a></li>
          <li><a href="/help/plugins">Editor Plugins</a></li>
          <li><a href="/help/floorc">~/.floorc.json</a></li>
          <li><a href="/help/floomatic">Floomatic</a></li>
          <li><a href="/help/flootty">FlooTTY</a></li>
        </ul>
      </div>

      <div class="col-md-3">
        <h5>Explore</h5>
        <ul>
          <li><a href="/active">Active Workspaces</a></li>
          <li><a href="/code_roulette">Code Roulette</a></li>
        </ul>
      </div>

      <div class="col-md-3">
        <h5>Talk to us</h5>
        <ul>
          <li><a href="irc://irc.freenode.net:6667/#floobits">IRC</a></li>
          <li><a href="https://twitter.com/Floobits">Twitter</a></li>
          <li><a id="ttu_email" href="">E-mail</a></li>
        </ul>
      </div>

      
<script type="text/javascript">
"use strict";
function handleWish (event) {
  debugger;
  var input, r, wish;
  event.preventDefault();
  input = $("wish-this-page-would-input");
  wish = input.val();
  input.val("");
  if (!wish || wish.length === 0) {
    return false;
  }
  r = new XMLHttpRequest();
  r.open("POST", "/wish", true);
  r.onreadystatechange = function () {
    if (r.readyState !== 4 || r.status !== 200) {
      return;
    }
    document.getElementById("wishing-well").innerHtml = r.responseText;
  };
  r.send("csrfmiddlewaretoken=" + encodeURIComponent(global.fl.csrfToken) +
    "&location=" + encodeURIComponent(global.location.href) +
    "&wish=" + encodeURIComponent(wish)
  );
  return false;
}
</script>
      <div id="wishing-well" class="col-md-6">
        <form id="wish-this-page-would" action="/wish" onsubmit="handleWish()" method="post">
          <input type='hidden' name='csrfmiddlewaretoken' value='AY7OQIDG8W8OnKTRmiKYndmxJdMX7PN9v1kYkbp793yQ41wWVi9LKmZdG2bdnRKE' />
          <label>
            I wish this page would
            <input name="wish" id="wish-this-page-would-input" placeholder="write my code for me"/>
          </label>
        </form>
      </div>
      
    </div>
  </div>
</div>
<script type="text/javascript">
document.getElementById("ttu_email").setAttribute("href", "mail" + "to:" + "in" + "fo" + "@" + "floo" + "bits.com");
</script>

    
  </main>
  <script type="text/javascript" src="/static/CACHE/js/ab140cc2f66f.js"></script>
  

<script type="text/javascript">
"use strict";
function update_wuc() {
  $.ajax({
    url: "/api/watch_us_code",
    type: "GET",
    success: function (data) {
      if (data && data.owner && data.name) {
        document.getElementById("watch-us-code-href").setAttribute("href", "/" + data.owner + "/" + data.name);
        $("#watch-us-code").show();
      } else {
        $("#watch-us-code").hide();
      }
    },
    error: function () {
      $("#watch-us-code").hide();
    },
  });
}
setInterval(update_wuc, 60000);
</script>
  
<script type="text/javascript">
_eventTracker.push(["user_funnel", "browse_room"]);
</script>

  
  
    <!-- begin olark code -->
<script data-cfasync="false" type="text/javascript">/*{literal}<![CDATA[*/window.olark||(function(c){var f=window,d=document,l=f.location.protocol=="https:"?"https:":"http:",z=c.name,r="load";var nt=function(){
f[z]=function(){
(a.s=a.s||[]).push(arguments)};var a=f[z]._={
},q=c.methods.length;while(q--){(function(n){f[z][n]=function(){
f[z]("call",n,arguments)}})(c.methods[q])}a.l=c.loader;a.i=nt;a.p={
0:+new Date};a.P=function(u){
a.p[u]=new Date-a.p[0]};function s(){
a.P(r);f[z](r)}f.addEventListener?f.addEventListener(r,s,false):f.attachEvent("on"+r,s);var ld=function(){function p(hd){
hd="head";return["<",hd,"></",hd,"><",i,' onl' + 'oad="var d=',g,";d.getElementsByTagName('head')[0].",j,"(d.",h,"('script')).",k,"='",l,"//",a.l,"'",'"',"></",i,">"].join("")}var i="body",m=d[i];if(!m){
return setTimeout(ld,100)}a.P(1);var j="appendChild",h="createElement",k="src",n=d[h]("div"),v=n[j](d[h](z)),b=d[h]("iframe"),g="document",e="domain",o;n.style.display="none";m.insertBefore(n,m.firstChild).id=z;b.frameBorder="0";b.id=z+"-loader";if(/MSIE[ ]+6/.test(navigator.userAgent)){
b.src="javascript:false"}b.allowTransparency="true";v[j](b);try{
b.contentWindow[g].open()}catch(w){
c[e]=d[e];o="javascript:var d="+g+".open();d.domain='"+d.domain+"';";b[k]=o+"void(0);"}try{
var t=b.contentWindow[g];t.write(p());t.close()}catch(x){
b[k]=o+'d.write("'+p().replace(/"/g,String.fromCharCode(92)+'"')+'");d.close();'}a.P(2)};ld()};nt()})({
loader: "static.olark.com/jsclient/loader0.js",name:"olark",methods:["configure","extend","declare","identify"]});
/* custom configuration goes here (www.olark.com/documentation) */
olark.identify('4228-476-10-5944');/*]]>{/literal}*/

olark('api.chat.updateVisitorNickname', {snippet: 'Oriel'});


olark('api.visitor.updateEmailAddress', {emailAddress: 'oriel1987@gmail.com'});


olark('api.visitor.updateCustomFields', {plan: 'Free'});

</script><noscript><p><a href="https://www.olark.com/site/4228-476-10-5944/contact" title="Contact us" target="_blank">Questions? Feedback?</a> powered by <a href="http://www.olark.com?welcome" title="Olark live chat software">Olark live chat software</a></p></noscript>
<!-- end olark code -->

  
  
  <script type="text/javascript">
var ii, _events;

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script', '//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-35691554-1', 'auto');
ga('require', 'ecommerce');
ga('send', 'pageview');
for (ii = 0; ii < _eventTracker.length; ii++) {
  _events = _eventTracker[ii];
  ga("send", "event", _events[0], _events[1], _events[2], _events[3], _events[4]);
}
</script>

  
  
</body>
</html>