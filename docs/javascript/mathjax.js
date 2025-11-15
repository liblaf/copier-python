// ref: <https://squidfunk.github.io/mkdocs-material/reference/math/#mathjax>

window.MathJax = {
	tex: {
		inlineMath: [["\\(", "\\)"]],
		displayMath: [["\\[", "\\]"]],
		processEscapes: true,
		processEnvironments: true,
		// ref: <https://docs.mathjax.org/en/v3.2/input/tex/extensions/physics.html#physics>
		packages: { "[+]": ["physics"] },
	},
	// ref: <https://docs.mathjax.org/en/v3.2/web/components/combined.html#tex-mml-chtml>
	loader: { load: ["tex-mml-chtml", "[tex]/physics"] },
	options: {
		ignoreHtmlClass: ".*|",
		processHtmlClass: "arithmatex",
	},
};

document$.subscribe(() => {
	MathJax.startup.output.clearCache();
	MathJax.typesetClear();
	MathJax.texReset();
	MathJax.typesetPromise();
});
