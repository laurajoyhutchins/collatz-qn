\
.PHONY: all counts fit plots residuals unpack verify clean-unpacked clean help

ZIP := data/raw/qn_exponents_package.zip
UNPACK_DIR := data/raw/unpacked

all: counts fit plots residuals

## Unzip raw package into a git-ignored folder
unpack: $(ZIP)
	@mkdir -p $(UNPACK_DIR)
	@command -v unzip >/dev/null 2>&1 || { echo "unzip not found"; exit 1; }
	unzip -o -q "$(ZIP)" -d "$(UNPACK_DIR)"
	@echo "Unpacked to $(UNPACK_DIR)"

## Verify ZIP integrity (optional)
verify: $(ZIP)
	@if [ -f data/raw/qn_exponents_package.sha256 ]; then \
		shasum -a 256 -c data/raw/qn_exponents_package.sha256; \
	else \
		echo "Checksum file missing: data/raw/qn_exponents_package.sha256"; exit 1; \
	fi


# Remove redundant 'data' alias; use 'counts' as main target
counts:
	@python -m scripts.compute_counts

fit: counts
	@python -m scripts.fit_zipf_models

plots: counts
	@python -m scripts.plot_figures

residuals:
	@python -m scripts.compute_and_plot_residuals


clean-unpacked:
	@rm -rf "$(UNPACK_DIR)"


clean:
	@rm -rf data/processed/*.csv figures/*.png results/*

# Help target
help:
	@echo "Available targets:"
	@echo "  all         - Run counts, fit, plots, residuals"
	@echo "  counts      - Compute counts (main data target)"
	@echo "  fit         - Fit Zipf models (depends on counts)"
	@echo "  plots       - Plot figures (depends on counts)"
	@echo "  residuals   - Compute and plot residuals"
	@echo "  unpack      - Unpack raw ZIP data"
	@echo "  verify      - Verify ZIP integrity (requires checksum file)"
	@echo "  clean       - Remove generated data and figures"
	@echo "  clean-unpacked - Remove unpacked raw data"
	@echo "  help        - Show this help message"
