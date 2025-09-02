// ref: <https://docs.readthedocs.com/platform/stable/intro/mkdocs.html#integrate-the-read-the-docs-version-menu-into-your-site-navigation>

document.addEventListener("DOMContentLoaded", (event) => {
	// Trigger Read the Docs' search addon instead of Material MkDocs default
	document.querySelector(".md-search__input").addEventListener("focus", (e) => {
		const event = new CustomEvent("readthedocs-search-show");
		document.dispatchEvent(event);
	});
});

// Use CustomEvent to generate the version selector
document.addEventListener("readthedocs-addons-data-ready", (event) => {
	const config = event.detail.data();
	const versioning = `
<div class="md-version">
<button class="md-version__current" aria-label="Select version">
    ${config.versions.current.slug}
</button>

<ul class="md-version__list">
${config.versions.active
	.map(
		(version) => `
    <li class="md-version__item">
    <a href="${version.urls.documentation}" class="md-version__link">
        ${version.slug}
    </a>
            </li>`,
	)
	.join("\n")}
</ul>
</div>`;

	// Check if we already added versions and remove them if so.
	// This happens when using the "Instant loading" feature.
	// See https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#instant-loading
	const currentVersions = document.querySelector(".md-version");
	if (currentVersions !== null) {
		currentVersions.remove();
	}
	document
		.querySelector(".md-header__topic")
		.insertAdjacentHTML("beforeend", versioning);
});
