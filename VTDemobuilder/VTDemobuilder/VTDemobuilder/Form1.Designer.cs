namespace VTDemobuilder
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.Id_Cell = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Name_Cell = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Rad_Cell = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Colour_Cell = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.textBox1 = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(374, 211);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(88, 29);
            this.button1.TabIndex = 0;
            this.button1.Text = "buildXML";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // dataGridView1
            // 
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.Id_Cell,
            this.Name_Cell,
            this.Rad_Cell,
            this.Colour_Cell});
            this.dataGridView1.Location = new System.Drawing.Point(12, 246);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.RowTemplate.Height = 24;
            this.dataGridView1.Size = new System.Drawing.Size(450, 178);
            this.dataGridView1.TabIndex = 1;
            // 
            // Id_Cell
            // 
            this.Id_Cell.HeaderText = "Id";
            this.Id_Cell.Name = "Id_Cell";
            // 
            // Name_Cell
            // 
            this.Name_Cell.HeaderText = "Name";
            this.Name_Cell.Name = "Name_Cell";
            // 
            // Rad_Cell
            // 
            this.Rad_Cell.HeaderText = "Radiation Limit";
            this.Rad_Cell.Name = "Rad_Cell";
            // 
            // Colour_Cell
            // 
            this.Colour_Cell.HeaderText = "Colour";
            this.Colour_Cell.Name = "Colour_Cell";
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(12, 12);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(350, 228);
            this.textBox1.TabIndex = 2;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(474, 436);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.dataGridView1);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.DataGridViewTextBoxColumn Id_Cell;
        private System.Windows.Forms.DataGridViewTextBoxColumn Name_Cell;
        private System.Windows.Forms.DataGridViewTextBoxColumn Rad_Cell;
        private System.Windows.Forms.DataGridViewTextBoxColumn Colour_Cell;
        private System.Windows.Forms.TextBox textBox1;
    }
}

